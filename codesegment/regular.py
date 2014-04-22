#!/usr/bin/env python
#encoding:utf8

import re

# match(): 判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
restr = r'(P|python)' #匹配P或者python
if re.match(restr, 'Python'):
    '''
    '''
    #print 'match'

m = re.match(restr, 'Python') #匹配到的是P
#print m.groups()

# split(): 正则表达式切分字符串比用固定的字符更灵活
re.split(r'\s+', 'a b  c')

# 分组, 正则中用()表示的就是要提取的分组
# \d{3,8}才是正确的写法, \d{3, 8}(中间多了一个空格)就不能匹配, 切记
merr = re.match(r'(\d{3})-(\d{3, 8})', '010-123456')
#print merr

m = re.match(r'(\d{3})-(\d{3,8})', '010-123456')
#注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串
#print m.groups()
#print m.group(1)

# 一个体现正在是贪婪匹配的例子
m = re.match(r'(\d+)(0*)', '123000')
#print m.groups()

# 为了提高正则的效率, 可以先对重复使用的正在进行编译
re_phone = re.compile(r'(\d{3})-(\d{3,8})')
m = re_phone.match('010-12345')

#<hello> demonlife2013@gmail.com
#demonlife2013@test.co.uk
re_email1 = re.compile(r'(?P<nametag>\<[a-zA-Z0-9 \.-]+\>\s?)*([a-zA-Z0-9_\.-]+)@([a-zA-z0-9]+)(\.\w+)*(\.[a-z]{1,})')
m1 = re_email1.match('demonlife2013@gmail.com')
#print m1.groups()
m2 = re_email1.match('<demonlife> demonlife2013@test.gmail.com')
#print m2.groups()
#print 'regulare group name: %s' % m2.group('nametag')
