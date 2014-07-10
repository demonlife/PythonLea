#encoding: utf8

import os, sys
import struct

picturs_path = r'/home/demon/Pictures'
def get_pics_path(picturs_path):
    for dpath, dname, fname in os.walk(picturs_path):
        if len(dname) > 0: # 有子目录，继续遍历
            for d in dname:
                get_pics_path(d)
            #
        #
        for f in fname:
            yield os.path.join(dpath, f)
        #
    #
#

for fname in get_pics_path(picturs_path):
    fdata = open(fname, 'r').read(30)
    pic_struct = struct.unpack('<ccIIIIIIHH', fdata)
    if pic_struct[0]+pic_struct[1] == 'BM' or \
       pic_struct[0]+pic_struct[1] == 'BA':
        print fname, 'is a bmp file'
    #
#
        
