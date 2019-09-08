#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce


def norm(s):
    return s.lower().capitalize()


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


l = ['administrator', 'geoGe', 'San Francisco']
print(list(map(norm, l)))

s = '23112312'
print(str2int(s))
