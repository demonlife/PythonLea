#encoding: utf8

import sys

x = 0x1234
print sys.getsizeof(x) #获取x所占用的内存
print sys.getrefcount(x) # 读取头部引用计数，形参也会增加一次引用, 在交互界面中输出2， 执行文件则输出4？

import types
#所有内置类型对象都可以在types模块中找到。
type(x) is types.IntType
print x.__class__
print x.__class__ is type(x) is int is types.IntType

globals()['y'] = 'hello world'
print y

import psutil, gc, os

def test():
    x = 0
    for i in range(10000000):
        x += i

    return x

def main():
    print test()
    gc.collect()
    p = psutil.Process(os.getpid())

    print p.get_memory_info()

import sys, locale
print reload(sys)
print 'python default encoding:', sys.getdefaultencoding()
c = locale.getdefaultlocale()
print 'current os encoding:', c
sys.setdefaultencoding(c[1])
    
