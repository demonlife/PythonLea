#!/usr/bin/env python
#encoding: utf8

def str2int(s):
    def fn(x, y):
        return x * 10 + y

    return reduce(fn, map(int, s))

def str2int2(s):
    return reduce(lambda x, y: x * 10 + y, map(int, s))

import collections

def my_map(f, *argsIt):
    '''
    '''
    for x in argsIt:
        if not isinstance(x, collections.Iterable):
            raise TypeError("argument must be a iterable")

    itCount = len(argsIt)
    itLen = len(argsIt[0])
    result = []
    for j in xrange(itLen):
        args = []
        for i in xrange(itCount):
            args.append(argsIt[i][j])
        result.append(f(*args))
    return result

#print my_map(lambda x, y: x * y, [1, 2, "a", 4], [1, 2, 3, 4])
#print my_map(lambda x, y: x * y, (1, 2, "a", 4), [1, 2, 3, 4])
#print map(lambda x, y: x * y, (1, 2, "a", 4), [1, 2, 3, 4])

