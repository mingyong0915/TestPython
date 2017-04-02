#!/usr/bin/env python  
# _*_ coding:utf-8 _*_

""" 
@version: v1.0 
@author: MingYong 
@license: Apache Licence  
@contact: 13760182207@163.com 
@site: http://blog.csdn.net/mingyong_blog 
@software: PyCharm 
@file: 001.py 
@time: 2017/4/2 22:31 
"""


class MyException(Exception):
    pass
myException = MyException("出错啦")
print myException

while True:
    try:
        x = input("Enter the first number:")
        y = input("Enter the second number:")
        value = x/y
        print "x/y is ", value
    except Exception, e:
        print "Invalid input ,please try again."
    else:
        break

# 函数处理异常


def faulty():
    raise Exception


def ignore_exception():
    faulty()


def handle_exception():
    try:
        faulty()
    except Exception:
        print "handle exception"
handle_exception()
