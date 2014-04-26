#!/usr/bin/env python
#encoding: utf8

#new-style class

class D(object):
    def foo(self):
        print "class D"

class B(D):
    pass

class C(D):
    def foo(self):
        print "class C"

class A(B, C):
    pass

A().foo() # class C

'''
# old-style class

class D:
    def foo(self):
        print "class D"

class B(D):
    pass

class C(D):
    def foo(self):
        print "class C"

class A(B, C):
    pass

A().foo()    
'''
