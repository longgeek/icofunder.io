#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
import qrcode


def gen(invite_code):
    qr = qrcode.QRCode(border=2,
                       version=1,
                       box_size=10,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,)
    qr.add_data(invite_code)
    img = qr.make(fit=True)
    img = qr.make_image(fill_color='#8980fe', back_color='#f5f5f5')
    img_name = '/tmp/%s.jpg' % str(uuid.uuid1())
    img.save(img_name)
    return img_name
