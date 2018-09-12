# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class GetOrNoneManager(models.Manager):
    """Adds get_or_none method to objects
    """
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None


class Invites(models.Model):
    email = models.EmailField(unique=True, verbose_name=_('邮箱'),
                              max_length=254)
    is_kyc = models.BooleanField(_("KYC 状态"), default=False)
    invited_at = models.DateTimeField(auto_now_add=True)
    invited_user = models.ForeignKey(User)
    objects = GetOrNoneManager()


class UserExtra(models.Model):
    user = models.ForeignKey(User)
    is_kyc = models.TextField(_("KYC 状态"), null=True, blank=True)
    eth_wallet = models.TextField(_("ETH 钱包"), null=True, blank=True)
    invests = models.TextField(_("投资"), null=True, blank=True)
    fullname = models.TextField(_("全名"), null=True, blank=True)
    password = models.TextField(_("密码"), null=True, blank=True)
    invite_code = models.IntegerField(_("邀请码"), null=True, blank=True)
    objects = GetOrNoneManager()
