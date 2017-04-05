#!/usr/bin/env python  
# _*_ coding:utf-8 _*_

""" 
@version: v1.0 
@author: MingYong 
@license: Apache Licence  
@contact: 13760182207@163.com 
@site: http://blog.csdn.net/mingyong_blog 
@software: PyCharm 
@file: 007.py 
@time: 2017/4/4 11:33 
"""

# random模块
from random import *
print random()

#getrandbits(n) #返回一个nbit位的整数
#uniform(a,b)

#randrange()
print randrange(9) #产生0到8
#choice(seq) 从一个序列seq中随机选择一个元素
#shuffle(seq) 对一个序列进行乱序排列
#sample(seq, n) 从序列seq中随机抽取n个元素

#创建52张牌
values = range(1,11,1) + "J Q K".split()
suits = "diamonds clubs spades hearts".split()
decs = ["%s of %s" %(v, s) for v in values for s in suits]
shuffle(decs)
while decs:
    print raw_input(decs.pop())
