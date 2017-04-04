#!/usr/bin/env python  
# _*_ coding:utf-8 _*_

""" 
@version: v1.0 
@author: MingYong 
@license: Apache Licence  
@contact: 13760182207@163.com 
@site: http://blog.csdn.net/mingyong_blog 
@software: PyCharm 
@file: 004.py 
@time: 2017/4/3 20:55 
"""

# 模块; 一个.py文件就是一个模块
# import 模块名
import sys
import pprint
import helloworld
pprint.pprint(sys.path)
#方法1
sys.path.append("../001.py")
#方法2，配置环境变量
#