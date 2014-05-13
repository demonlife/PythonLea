#encoding: utf8

# 代码原始地址： http://blog.jobbole.com/54057/
import time

'''
def timefunc(f):
    def f_timer(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time();
        print f.__name__, 'took', end - start, 'time'
        return result
    return f_timer

def get_number():
    for x in xrange(5000000):
        yield x

@timefunc
def expensive_function():
    for x in get_number():
        i = x ^ x ^x
    return 'some result!'

result = expensive_function()
'''

'''
#使用上下文来检查时间使用情况
class timewith():
    def __init__(self, name = ''):
        self.name = name
        self.start = time.time()

    @property
    def elapsed(self):
        return time.time() - self.start

    def checkpoint(self, name=""):
        print '{timer} {checkpoint} took {elapsed} seconds'.format(
            timer = self.name,
            checkpoint = name,
            elapsed = self.elapsed,
            ).strip()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.checkpoint('finished')

def get_number():
    for x in xrange(5000000):
        yield x

def expensive_function():
    for x in get_number():
        i = x ^ x ^ x
    return 'some result'

with timewith('fancy thing') as timer:
    expensive_function()
    timer.checkpoint('done with something')
    expensive_function()
    expensive_function()
    timer.checkpoint('done with something else')

# directly use
timer = timewith('fancy thing')
expensive_function()
timer.checkpoint('done with something')
'''

# 使用内建优化器
import cProfile

def do_cprofile(func):
    def profield_func(*args, **kwargs):
        profile = cProfile.Profile()
        try:
            profile.enable()
            result = func(*args, **kwargs)
            profile.disable()
            return result
        finally:
            profile.print_stats()
    return profield_func

def get_number():
    for x in xrange(5000000):
        yield x

@do_cprofile
def expensive_function():
    for x in get_number():
        i = x ^ x ^ x
    return 'some result'

result = expensive_function()
        
    

    
