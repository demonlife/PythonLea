#!/usr/bin/env python
#encoding: utf8

import os
os.system('ls -l /proc/cpuinfo') #程序无法获取输出和返回值

out = os.popen("ls -l /proc/cpuinfo") # 调用系统命令，获取命令输出不能得到返回值
print out.read()

import commands
# 调用系统命令，获取命令输出和返回值
r = commands.getstatusoutput('ls -l /proc/cpuinfo')
print r

