#!/usr/bin/env python
#encoding: utf8

import re

'''
numbers = ["123 555 6789",
            "1-(123)-555-6789",
            "(123-555-6789",
            "(123).555.6789",
            "123 55 6789",
            "1.(123)-555-6789",
            "1 (124)-555-6789",
            "1  (123)-555-6789",]

for number in numbers:
    pattern = re.match(r'^'
                    r'(1[-\s.])?'           # optional '1-', '1.' or '1'
                    r'(\()?'                # optional opening parenthesis
                    r'\d{3}'                # the area code
                    r'(?(2)\))'             # if there was opening parenthesis, close it
                    r'[-\s.]?'              # followed by '-' or '.' or space
                    r'\d{3}'                # first 3 digits
                    r'[-\s.]?'              # followed by '-' or '.' or space
                    r'\d{4}$\s*',number, re.DEBUG)
    if pattern:
        print '{0} is valid'.format(number)
    else:
        print '{0} is not valid'.format(number)
'''

'''
# greedy and ungreedy
html = 'Hello <a href="http://pryix.com" title="pypix">Pypix</a>' \
'Hello <a href="http://example.com" title"example">example</a>'
m = re.findall("<a.*>.*<\/a>", html) #greedy
m = re.findall("<a.*?>.*?<\/a>", html) #ungreedy
if m:
    print m
'''

'''
#lookahead and lookebehind
strings = ["hello foo",
           "hello foobar", ]
for string in strings:
    #pattern = re.search(r'foo(?=bar)', string) #lookbehind which has a bar
    pattern = re.search(r'(?<=foo)bar', string) #lookahead which has a foo
    if pattern:
        print 'lookahead True: ', pattern
    else:
        print 'lookahead False: ', pattern

strings = ["hello foo",
           "hello foobar",
           "hello foobaz",
           "hello bazbar", ]
for string in strings:
    #pattern = re.search(r'foo(?!bar)', string) #lookbehind wihch not has bar
    pattern = re.search(r'(?<!foo)bar', string) #lookahead wihch not has bar
    if pattern:
        print 'True'
    else:
        print 'False'
'''

'''
#coditional
strings = [ "<pypix>",
            "<foo",
            "bar>",
            "hello", ]
for string in strings:
    pattern = re.search(r'^(<)?[a-z]+(?(1)>)$', string)
    if pattern:
        print 'True'
    else:
        print 'False'
        '''
'''
# not caputer
string = "Hello foobar"
#pattern = re.search(r'(H.*)(f.*)(b.*)', string)
pattern = re.search(r'(?:H.*)(f.*)(b.*)', string) #not caputre H.*
print "f* => {0}".format(pattern.group(1))
print "b* => {0}".format(pattern.group(2))
'''

'''
# named subpatterns
string = "hello foobar"
pattern = re.search(r'(?P<fstart>f.*)(?P<bstart>b.*)', string)
print "f* => {0}".format(pattern.group('fstart'))
print "b* => {0}".format(pattern.group('bstart'))
'''

#callback

template = "Hello [first_name] [last_name],\
Thank you for purchasing [product_name] from [store_name].\
The total cost of your purchase was [product_price] plus [ship_price] for shipping.\
You can expect your product to arrive in [ship_days_min] to [ship_days_max] business days.\
Sincerely, [store_manager_name]"

dic = {
    "first_name": "John",
    "last_name": "Doe",
    "product_name": "iphone",
    "store_name" : "Walkers",          
    "product_price": "$500",          
    "ship_price": "$10",          
    "ship_days_min": "1",          
    "ship_days_max": "5",          
    "store_manager_name": "DoeJohn"          
}          

result = re.compile(r'\[(.*)\]')
#print result.sub("John", template, count=1)

def multiple_replace(dic, text):
    pattern = "|".join(map(lambda key: re.escape("[" + key + "]"), dic.keys()))
    return re.sub(pattern, lambda m: dic[m.group()[1:-1]], text)
print multiple_replace(dic, template)
