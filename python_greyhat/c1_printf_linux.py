#!/usr/bin/env python
# coding:utf-8

# P7 - for linux,cannot run in windows
from ctypes import *
libc = CDLL("libc.so.6")
message_string = "Hello blackhat python!-Linux\n"
libc.printf("Testing:%s",message_string)


