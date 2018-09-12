#!/usr/bin/env python
# -*- coding: utf-8 -*-

from icofunder.apphome import models
from icofunder.lib import gen_invite_code


def record(request):
    """
        IN THE LOGIN, TO RECORD USER PASSWORD.
        change the allauth/account/forms.py line 199:

        from icofunder.lib import record_password
        record_password.record(self.request)

    """
    try:
        request.user_id
    except:
        return
    password = request.POST.dict()['password']
    user_extra = models.UserExtra.objects.get_or_none(
        user_id=request.user.id
    )
    if user_extra is None:
        user_extra = models.UserExtra.objects.create(
            user_id=request.user.id,
            password=password,
            invite_code=gen_invite_code.gen(),
        )
    else:
        user_extra.password = password
        user_extra.save()
