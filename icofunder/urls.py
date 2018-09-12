"""icofunder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.i18n import javascript_catalog
from django.views.generic.base import RedirectView
from icofunder.apphome import views
from icofunder.lib.icos import PROJECTS


js_info_dict = {
    'packages': ('languages', )
}

project_name = '|'.join([category for category in PROJECTS.keys()])

urlpatterns = i18n_patterns(
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^(?P<project_name>%s)/$' % project_name, views.project_detail),
    url(r'^ref/([0-9]{6,10})/$', views.ref),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^kyc/$', views.kyc, name='kyc'),
    url(r'^kyc/upload/$', views.kyc_upload),
    url(r'^kyc/set/$', views.kyc_set),
    url(r'^kyc/status/(.+)/$', views.kyc_status, name='kyc_status'),
    url(r'^eth/wallet/$', views.eth_wallet),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/user/extra/$', views.get_user_extra),
    url(r'^accounts/invite/$', views.invite, name='invite'),
    url(r'^accounts/invite/poster/$', views.invite_poster, name='invite_poster'),
    url(r'^accounts/invite/poster/maker$', views.invite_poster_maker),
    url(r'^accounts/invest/$', views.invest, name='invest'),
    url(r'^accounts/invest/transactions/$', views.invest_transactions),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^how/$', views.how, name='how'),
    url(r'^about/$', views.about, name='about'),
    url(r'^token/$', views.token, name='token'),
    url(r'^ico/ended/$', views.ended, name='ico-ended'),
    url(r'^ico/ongoing/$', views.ongoing, name='ico-ongoing'),
    url(r'^ico/upcoming/$', views.upcoming, name='ico-upcoming'),
    url(r'^favicon.ico$', RedirectView.as_view(url=r'/static/favicon.ico')),
    url(r'^terms/$', views.terms, name='terms'),
    url(r'^cookie/$', views.cookie, name='cookie'),
    url(r'^ratings/$', views.ratings, name='ratings'),
    url(r'^privacy/$', views.privacy, name='privacy'),
    url(r'^disclaimer/$', views.disclaimer, name='disclaimer'),
    url(r'^jsi18n/', javascript_catalog, js_info_dict, name='jsi18n'),
    prefix_default_language=False
)
