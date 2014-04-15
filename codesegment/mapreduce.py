#!/usr/bin/env python
#encoding: utf8

def str2int(s):
    def fn(x, y):
        return x * 10 + y

    return reduce(fn, map(int, s))

def str2int2(s):
    return reduce(lambda x, y: x * 10 + y, map(int, s))
