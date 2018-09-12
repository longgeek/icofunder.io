#!/usr/bin/env python
# -*- coding: utf-8 -*-

from icofunder.apphome import models


def gen():
    user_extra_list = models.UserExtra.objects.all()
    if len(user_extra_list) == 0:
        invite_code = 631800
    else:
        invite_code = models.UserExtra.objects.last().invite_code + 1
    return invite_code
