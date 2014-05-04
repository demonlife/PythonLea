#!/usr/bin/env python
#encoding: utf8

#代码原地址：http://late.am/post/2012/03/26/exploring-python-code-objects
'''
code_str1 = """
print "hello, world"
"""

code_obj1 = compile(code_str1, '<string>', 'exec')
exec(code_obj1)

code_obj2 = compile(code_str1, '<string>', 'single')
exec(code_obj2)

#compile fail
#code_obj3 = compile(code_str1, '<string>', 'eval') 

code_str2 = """
print 'Hello, world'
print 'goodbye, world'
"""

code_obj4 = compile(code_str2, '<string>', 'exec')
exec(code_obj4)

code_obj5 = compile(code_str2, '<string>', 'single')
exec(code_obj5)
'''

code_str = """
print 'hello, world'
"""

code_obj = compile(code_str, 'string', 'exec')
#print dir(code_obj)
print code_obj.co_filename
print code_obj.co_name
print code_obj.co_firstlineno



