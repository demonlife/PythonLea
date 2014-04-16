#!/usr/bin/env python
#encoding: utf8

'''
使用metaclass给自定义的MyList增加一个add方法

ORM是使用metaclass的一个典型例子, 参见:
https://raw.githubusercontent.com/michaelliao/learn-python/master/metaclass/simple_orm.py
'''

#metaclass是创建类，所以必须从`type`类型派生
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list):
    #它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建
    '''
    __new__()方法接收到的参数依次是：
    当前准备创建的类的对象；
    类的名字；
    类继承的父类集合；
    类的方法集合。
    '''
    __metaclass__ = ListMetaclass #指示使用ListMetaclass来定制类
    
