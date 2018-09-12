#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pytz
import datetime

from hashlib import md5
from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def gen_gravatar_url(email, size="100"):
    url = "https://secure.gravatar.com/avatar/%s?size=%s&default=identicon&rating=pg"
    return url % (md5(email.lower()).hexdigest(), size)


@register.simple_tag
def invites_candy(invites, invites_kyc):
    return len(invites) * 200 + len(invites_kyc) * 300 + 500


@register.simple_tag
def invites_price(invites, invites_kyc):
    candy = len(invites) * 200 + len(invites_kyc) * 300 + 500
    return "%.4f" % (candy * 1 / 6.3)


@register.simple_tag
def eth_amount(amount):
    return (float(amount) / 1000000000000000000.0)


@register.simple_tag
def convert_date(date, request):
    if request.LANGUAGE_CODE == 'zh-hans':
        tz = pytz.timezone('Asia/Shanghai')
        format = '%Y-%m-%d %H:%M:%S'
        local_time = datetime.datetime.fromtimestamp(
            int(date), tz).strftime(format)
    else:
        l_time = time.localtime(float(date))
        local_time = time.strftime("%b-%d-%Y %H:%M:%S", l_time)
    return local_time


# Settings value
@register.simple_tag
def SETTINGS(name):
    return getattr(settings, name, "")


# Switch languare
@register.simple_tag
def switch_lang(request, lang):
    url = request.get_full_path()
    if lang == 'zh-hans' and url.startswith('/en'):
        url = url[3:]
    elif lang == 'en' and url.startswith('/en') is False:
        url = '/en' + url
    return url
