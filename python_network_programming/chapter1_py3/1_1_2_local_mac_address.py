#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/3/19 18:04'

"""
https://www.cnblogs.com/chenjingyi/p/5741742.html
"""

import uuid


def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0, 11, 2)])


if __name__ == '__main__':
    print(get_mac_address())