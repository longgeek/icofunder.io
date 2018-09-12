#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from ethereum import utils


def gen():
    private_key = utils.sha3(os.urandom(4096))
    raw_address = utils.privtoaddr(private_key)
    account_address = utils.checksum_encode(raw_address)
    return (account_address, private_key.encode('hex'))
