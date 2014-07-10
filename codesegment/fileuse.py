#encoding: utf8

import os, glob

# 获取当前文件的决定路径
path_str = os.path.abspath(os.path.dirname(__file__))

# 获取路径中的文件名
bname = os.path.basename(path_str)

# 获取路径中的路径名
dname = os.path.dirname(path_str)

# 列出当前路径下的文件以及文件名
def mylistdir(dname):
    for fname in os.listdir(dname):
        print fname
    #
#

# 使用glob模块， 设置文件过滤
def myglob(path_str):
    for fname in glob.glob(path_str+'/*.py'):
        print fname
    #
#

# 遍历当前目录下的所有文件
files_cnt1 = 0
def processDirectory(args, dirname, filenames):
    for fname in filenames:
        path_str = os.path.join(dirname, fname)
        if not os.path.exists(path_str):
            print 'file is not exists, path=', path_str
        else:
            global files_cnt1
            files_cnt1 += 1
    #
#
os.path.walk(dname, processDirectory, None)

# 非递归的遍历
files_cnt2 = 0
def mywalk(dname):
    global files_cnt2
    for dirpath, dirnames, filenames in os.walk(dname):
        if len(dirnames) > 0:
            for d in dirnames:
                files_cnt2 += 1
                mywalk(d)
            #
        #if end
        for f in filenames:
            path_str = os.path.join(dirpath, f)
            if not os.path.exists(path_str):
                print 'not exists file, file name = ', path_str
            else:
                files_cnt2 += 1
            # for end
        # if end
    # for end
#def end
mywalk(dname)
print 'files cnt = ', files_cnt1
print 'files cnt = ', files_cnt2
    

