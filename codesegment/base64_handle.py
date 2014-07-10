#encoding: utf8

import base64

base64_str = base64.b64encode('str')
print base64_str
print base64.b64decode(base64_str)

def base64decode(base64_str):
    str_len = len(base64_str)
    add_len = str_len % 4
    base64_str += '='*(4 - add_len)
    return base64.b64decode(base64_str)

base64_noeql = base64_str.strip('=')
print base64decode(base64_noeql)

