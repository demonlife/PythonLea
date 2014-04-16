#!/usr/bin/env python
#encoding: utf8

import types

if type('abc') == types.StringType:
    '''
    '''
    #print 'the type is String'

#print type(int)
#print type(int) == types.TypeType

class Student(object):
    pass

s = Student()
s.name = 'Michael'

def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s, Student) #给实例绑定一个方法, 但是另一个实例是没有该方法的

def set_score(self, score):
    self.score = score

Student.set_score = MethodType(set_score, None, Student) #给类绑定方法, 所有的实例都可以访问该方法

class Teacher(object):
    __slots__ = ('name', 'age') #用tuple定义允许绑定的属性名称

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        print 'setter: ', value
        self._score = value

t = Teacher()
#t.score = 11 #error, 不调用t.score就不会出现错误, 否则会出现错误
#不能使用t.score的原因是: __slots__没有定义_score属性

class Chain(object):
    def __init__(self, path = ''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

print Chain().status.user.timeline.list #=> /status/user/timeline/list

# 源码: http://photo.weibo.com/1795308214/wbphotos/large/mid/3689075347236847/pid/6b023ab6tw1eeilk8cw5hj20xi0l442y
class XChain(object):
    def __init__(self, attr = ''):
        self._attr = attr

    def __getattr__(self, attr):
        print 'self._attr: %s, attr: %s' %(self._attr, attr)
        return XChain('%s/%s' % (self._attr, attr))

    def __str__(self):
        return self._attr

    def __call__(self, arg0 = ''):
        print '__call__ %s(%s)' %(self._attr, arg0)
        return XChain('%s/%s' % (self._attr, arg0))
        
#print XChain().users('abc').repos #=> /users/abc/repos

def fn(self, name="world"):
    print 'Hello, %s' % name

Hello = type('Hello', (object,), dict(hello=fn)) #创建Hello的类
#要创建一个class对象，type()函数依次传入3个参数：
#class的名称；
#继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上
#通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class
    

    


    
