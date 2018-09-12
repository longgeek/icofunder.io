# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

from icofunder.lib import icos
from icofunder.lib import gen_invite_code
from icofunder.lib import gen_eth_address
from icofunder.lib import list_average_slice
from icofunder.lib import gen_invite_qrcode
from icofunder.lib import gen_invite_poster
from icofunder.apphome import models
from icofunder.settings import NOTIFI_EMAIL, DEFAULT_FROM_EMAIL, ETHERSCAN_API_KEY

import os
import uuid
import base64
import requests
import datetime
import simplejson as json


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def home(request):
    content = {'ICOS': icos.ICOS, 'request': request}
    return render_to_response('index.html', content)


@login_required
def get_user_extra(request):
    if request.is_ajax() is False:
        return HttpResponseRedirect(reverse_lazy('home'))
    user_extra = models.UserExtra.objects.get_or_none(
        user_id=request.user.id
    )
    if user_extra is None:
        return HttpResponse("None")
    return HttpResponse(user_extra.is_kyc)


@login_required
def profile(request):
    content = {'ICOS': icos.ICOS, 'request': request}
    ref = request.COOKIES.get('ref')
    user_extra = models.UserExtra.objects.get_or_none(
        user_id=request.user.id
    )
    if user_extra is None:
        user_extra = models.UserExtra.objects.create(
            user_id=request.user.id,
            invite_code=gen_invite_code.gen(),
        )
    content['user_extra'] = user_extra
    response = render_to_response('profile.html', content)

    if ref is not None and ref != user_extra.invite_code:
        invite_user = models.UserExtra.objects.get_or_none(invite_code=ref)
        if invite_user is not None:
            invite_user = invite_user.user_id
            models.Invites.objects.create(
                is_kyc=False,
                email=request.user.email,
                invited_user_id=invite_user,
                invited_at=datetime.datetime.now()
            )
            response.delete_cookie('ref')
    return response


def ref(request, ref):
    url = 'home'
    if bool(request.user.is_authenticated) is False:
        url = 'account_signup'

    response = HttpResponseRedirect(reverse_lazy(url))
    response.set_cookie('ref', ref)
    return response


def faq(request):
    content = {'request': request}
    return render_to_response('faq.html', content)


@login_required
def invite(request):
    content = {'request': request}
    user_extra = models.UserExtra.objects.get_or_none(
        user_id=request.user.id
    )
    if user_extra:
        invite_code = user_extra.invite_code
        if invite_code is None:
            user_extra.invite_code = gen_invite_code.gen()
            user_extra.save()
    else:
        models.UserExtra.objects.create(user_id=request.user.id,
                                        invite_code=gen_invite_code.gen(),)
    invites = models.Invites.objects.filter(
        invited_user_id=request.user.id
    )
    invites_kyc = models.Invites.objects.filter(
        is_kyc=True,
        invited_user_id=request.user.id
    )
    url = "%s/ref/%s" % (
        request.get_raw_uri().split(request.path)[0],
        invite_code
    )
    content['invites'] = invites
    content['invites_kyc'] = invites_kyc
    content['invite_code'] = url
    return render_to_response('invite.html', content)


@login_required
def invite_poster_maker(request):
    content = {'request': request}
    return render_to_response('invite-poster.html', content)


@login_required
def invite_poster(request):
    if request.is_ajax() is False:
        return HttpResponseRedirect(reverse_lazy('home'))
    content = {'request': request}
    lang = request.POST.get('lang')
    invite_code = request.POST.get('invite_code')
    invite_qrcode = gen_invite_qrcode.gen(invite_code)
    invite_poster = '%s/static/images/poster/invite-%s.png' % (BASE_DIR, lang)
    poster_base64 = gen_invite_poster.gen(invite_poster, invite_qrcode)
    content['poster'] = poster_base64
    content['poster_uuid'] = str(uuid.uuid1())
    return render_to_response('invite-poster-modal.html', content)


def kyc(request):
    user_extra = models.UserExtra.objects.get_or_none(
        user_id=request.user.id
    )
    content = {"user_extra": user_extra, "request": request, "ICOS": icos.ICOS}
    return render_to_response('kyc.html', content)


@login_required
def kyc_upload(request):
    if request.is_ajax() is False:
        return HttpResponseRedirect(reverse_lazy('home'))
    fullname = request.POST.get('fullname')
    i_path = '%s/%s/' % ('KYC', request.user.id)
    d_path = '%s/%s__%s__%s__%s/' % ('KYC',
                                     request.user.id,
                                     request.user.username,
                                     request.user.email, fullname)
    if not os.path.exists(d_path):
        os.makedirs(d_path)
    if not os.path.exists(i_path):
        os.makedirs(i_path)
    image1 = request.FILES.getlist('image1')
    image2 = request.FILES.getlist('image2')
    image3 = request.FILES.getlist('image3')
    files = image1 + image2 + image3
    for f in files:
        destination = open(i_path + f.name, 'wb+')
        for chunk in f.chunks():
            destination.write(chunk)
        destination.close()
    user_extra = models.UserExtra.objects.get(user_id=request.user.id)
    user_extra.is_kyc = 'progress'
    user_extra.fullname = fullname
    user_extra.save()

    # Send Email
    send_mail(
        '用户 %s 请求 KYC 认证' % request.user.id,
        d_path,
        DEFAULT_FROM_EMAIL,
        [NOTIFI_EMAIL],
        fail_silently=False
    )
    return HttpResponse('ok')


@login_required
def kyc_set(request):
    if request.is_ajax() is False:
        return HttpResponseRedirect(reverse_lazy('home'))
    user_id = request.POST.get('user_id')
    kyc_status = request.POST.get('kyc_status')
    user = models.User.objects.get(id=user_id)
    user_extra = models.UserExtra.objects.get(user_id=user_id)
    if kyc_status == 'true':
        invites = models.Invites.objects.get_or_none(email=user.email)
        if invites is not None:
            invites.is_kyc = True
            invites.save()
    user_extra.is_kyc = kyc_status
    user_extra.save()
    return HttpResponse('ok')


@login_required
def kyc_status(request, user_id):
    if request.user.id != 1:
        return HttpResponseRedirect(reverse_lazy('home'))

    content = {'request': request}
    try:
        user = models.User.objects.get(id=user_id)
    except:
        user = None
        return render_to_response('kyc-status.html', content)
    user_extra = models.UserExtra.objects.get(user_id=user_id)
    user_invites = models.Invites.objects.get_or_none(email=user.email)
    content['user'] = user
    content['user_extra'] = user_extra
    content['user_invites'] = user_invites
    content['kyc_images'] = []

    if user_extra.is_kyc is not None or user_extra.is_kyc is not 'None':
        i_path = "KYC/%s" % user.id
        if os.path.exists(i_path):
            images = os.listdir(i_path)
            for img in images:
                img_path = "%s/%s" % (i_path, img)
                f = open(img_path, 'rb')
                c = base64.b64encode(f.read())
                f.close()
                content['kyc_images'].append(c)
    return render_to_response('kyc-status.html', content)


@login_required
def eth_wallet(request):
    if request.is_ajax() is False:
        return HttpResponseRedirect(reverse_lazy('home'))
    eth_wallet = request.POST.get('eth_wallet')
    user_extra = models.UserExtra.objects.get(user_id=request.user.id)
    user_extra.eth_wallet = eth_wallet
    user_extra.save()
    return HttpResponse('ok')


@login_required
def invest(request):
    user_extra = models.UserExtra.objects.get(
        user_id=request.user.id
    )
    content = {
        'ICOS': icos.ICOS,
        'request': request,
        'user_extra': user_extra
    }
    if user_extra.eth_wallet is None:
        return render_to_response('invest.html', content)

    wallet_get_url = "https://api.ethplorer.io/getAddressInfo/%s?apiKey=freekey" % user_extra.eth_wallet
    wallet_response = requests.get(url=wallet_get_url, verify=False)
    if wallet_response.status_code == 200:
        content['ethplorer'] = json.loads(wallet_response.text)

    # 生成所有项目的单独打币地址
    if user_extra.invests is None:
        invests = {}
        for p in icos.PROJECTS:
            invests[p] = gen_eth_address.gen()
        user_extra.invests = json.dumps(invests)
        user_extra.save()
        return render_to_response('invest.html', content)

    # 判断有没有新的项目加入
    invests = json.loads(user_extra.invests)

    invests_address = []
    for p in icos.PROJECTS:
        if p not in invests:
            invests[p] = gen_eth_address.gen()
        invests_address.append(invests[p][0])
    user_extra.invests = json.dumps(invests)
    user_extra.save()

    # etherscan.io api 限制每次最多查询 20 个地址
    # 把所有项目的钱包地址平均分片去查询
    # [
    #     {
    #         "account": "0x2c957a57214930e08Fc3b8F5CDE4F74a878C4249",
    #         "balance": "4221358600000000"
    #     }
    # ]
    all_address = []
    invests_address_slice = list_average_slice.gen(invests_address, 20)
    for i in invests_address_slice:
        multi_address = ','.join(i)
        tx_get_url = "https://api.etherscan.io/api?module=account&action=balancemulti&address=%s&tag=latest&apikey=%s" % (multi_address, ETHERSCAN_API_KEY)
        tx_response = requests.get(url=tx_get_url, verify=False)
        if tx_response.status_code == 200:
            all_address += json.loads(tx_response.text)['result']

    totals = {'number': 0, 'amount': 0}
    ongoing = content['ICOS']['ongoing']
    for ico in ongoing:
        invest = ico.values()[0]
        invest['AMOUNT'] = 0
        invest['ADDRESS'] = invests[ico.keys()[0]][0]
        for tx in all_address:
            if tx['account'] == invest['ADDRESS']:
                invest['AMOUNT'] += float(tx['balance']) / 1000000000000000000.0
                if invest['AMOUNT'] > 0:
                    totals['number'] += 1
                totals['amount'] += invest['AMOUNT']

    ended = content['ICOS']['ended']
    for ico in ended:
        invest = ico.values()[0]
        invest['AMOUNT'] = 0
        invest['ADDRESS'] = invests[ico.keys()[0]][0]
        for tx in all_address:
            if tx['account'] == invest['ADDRESS']:
                invest['AMOUNT'] += float(tx['balance']) / 1000000000000000000.0
                if invest['AMOUNT'] > 0:
                    totals['number'] += 1
                totals['amount'] += invest['AMOUNT']
    content['totals'] = totals
    return render_to_response('invest.html', content)


@login_required
def invest_transactions(request):
    if request.is_ajax() is False:
        return HttpResponseRedirect(reverse_lazy('home'))
    content = {
        'request': request
    }
    address = request.POST.get('address')
    tx_get_url = "https://api.etherscan.io/api?module=account&action=txlist&address=%s&startblock=0&endblock=99999999&sort=asc&apikey=SX63EZQIGM8CWA8NHVWHZXIZ5HABRK4S9X" % address
    tx_response = requests.get(url=tx_get_url, verify=False)
    if tx_response.status_code == 200:
        content['txs'] = json.loads(tx_response.text)['result']
    return render_to_response('invest-transactions.html', content)


def project_detail(request, project_name):
    p_type = icos.PROJECTS[project_name][0]
    p_index = icos.PROJECTS[project_name][1]
    content = {
        'request': request,
        'detail': icos.ICOS[p_type][p_index][project_name],
        'status': p_type,
    }

    if bool(request.user.is_authenticated):
        user_extra = models.UserExtra.objects.get_or_none(
            user_id=request.user.id
        )
        content['user_extra'] = user_extra
        if user_extra.invests is None:
            invests = {}
            invests[project_name] = gen_eth_address.gen()
            user_extra.invests = json.dumps(invests)
            user_extra.save()
        elif project_name not in json.loads(user_extra.invests):
            invests = json.loads(user_extra.invests)
            invests[project_name] = gen_eth_address.gen()
            user_extra.invests = json.dumps(invests)
            user_extra.save()
        else:
            invests = json.loads(user_extra.invests)
        content['address'] = invests[project_name][0]
    return render_to_response('project-details.html', content)


def ended(request):
    content = {
        'request': request,
        'ICOS': icos.ICOS,
    }
    return render_to_response('ended.html', content)


def ongoing(request):
    content = {
        'request': request,
        'ICOS': icos.ICOS,
    }
    return render_to_response('ongoing.html', content)


def upcoming(request):
    content = {
        'request': request,
        'ICOS': icos.ICOS,
    }
    return render_to_response('upcoming.html', content)


def how(request):
    content = {'request': request}
    return render_to_response('how-to-ico.html', content)


def about(request):
    content = {'request': request}
    return render_to_response('about.html', content)


def token(request):
    content = {'request': request}
    return render_to_response('token.html', content)


def terms(request):
    content = {'request': request}
    return render_to_response(
        'terms-%s.html' % request.LANGUAGE_CODE,
        content
    )


def cookie(request):
    content = {'request': request}
    return render_to_response(
        'cookie-%s.html' % request.LANGUAGE_CODE,
        content
    )


def ratings(request):
    content = {'request': request}
    return render_to_response(
        'ratings-%s.html' % request.LANGUAGE_CODE,
        content
    )


def privacy(request):
    content = {'request': request}
    return render_to_response(
        'privacy-%s.html' % request.LANGUAGE_CODE,
        content
    )


def disclaimer(request):
    content = {'request': request}
    return render_to_response(
        'disclaimer-%s.html' % request.LANGUAGE_CODE,
        content
    )
