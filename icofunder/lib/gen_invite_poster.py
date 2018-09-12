#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64

from PIL import Image
from io import BytesIO


def gen(poster_path, qrcode_path):
    """
        根据海报底图和用户邀请链接二维码生成海报
    :params poster_path, 海报底图路径
    :params qrcode_path, 邀请二维码路径
    :return, BASE64 图片内容

    """
    poster_img = Image.open(poster_path)
    qrcode_box = (385, 1260)
    qrcode_img = Image.open(qrcode_path).resize((210, 210), Image.ANTIALIAS)
    region = qrcode_img
    poster_img.paste(region, qrcode_box)

    # 把合成的海报转换为 Base64
    output = BytesIO()
    poster_img.save(output, format='JPEG')
    poster_data = output.getvalue()
    poster_base64 = 'data:image/jpg;base64,' + base64.b64encode(poster_data)
    return poster_base64


if __name__ == "__main__":
    gen('/opt/git/icofunder/icofunder/static/images/poster/invite-zh-hans.png', '/tmp/a.png')
