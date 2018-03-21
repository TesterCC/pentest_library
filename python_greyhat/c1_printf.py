#!/usr/bin/env python
# coding:utf-8

# P6 - for windows
from ctypes import *
msvcrt = cdll.msvcrt
message_string = "Hello blackhat python!-Windows\n"
msvcrt.printf("Testing:%s",message_string)


