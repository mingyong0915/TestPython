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