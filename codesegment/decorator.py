#!/usr/bin/env python
#encoding: utf8

import functools

def log(func_text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print 'begin call'
            func(*args, **kwargs)
            print 'end call'
        return wrapper

    def decorator2():
        @functools.wraps(func_text)
        def wrapper(*args, **kwargs):
            print 'begin call'
            func_text(*args, **kwargs)
            print 'end call'
        return wrapper

    if hasattr(func_text, '__call__'):
        return decorator2()
    else:
        return decorator

@log('execute')
def now():
    print 'now function call'
now()

@log
def now2():
    print 'now2 function call'
now2()

