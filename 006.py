#!/usr/bin/env python  
# _*_ coding:utf-8 _*_

""" 
@version: v1.0 
@author: MingYong 
@license: Apache Licence  
@contact: 13760182207@163.com 
@site: http://blog.csdn.net/mingyong_blog 
@software: PyCharm 
@file: 006.py 
@time: 2017/4/4 10:01 
"""

# python的集合、堆、双端队列
# set()
print set(range(10))
print set([0, 1, 2, 3, 0, 1, 2])
print set(['fee', 'fie', 'foe', 'fee'])
a = set([1, 2, 3])
b = set([2, 3, 4])
print a.union(b)  #a.union(b)与 a | b等价
print a | b
c = a & b
print c #set([2,3])

c.issubset(b) #判断c是不是b的子集
#或 c <= b
c.issuperset(b)#c是不是b的父集

a.intersection(b)
a.difference(b)
a.symmetric_difference(b)

# 堆
from heapq import *
from random import shuffle
data = range(10)
shuffle(data)
heap = []
for n in data:
    heappush(heap, n)
print heap
print heappop(heap)
print heap
print heappop(heap)
print heap

# 将一个序列变成堆序列
seq = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2]
heapify(seq)
print seq
heapreplace(seq, 2.5) #弹出最顶的元素，同时向堆中加入新元素2.5

#双端队列： 在collections 模块中的deque
from collections import deque

q = deque(range(5))
print q
q.append(5) #从后添加元素
q.appendleft(6) #从前面加元素
q.pop() #弹出右边的元素
q.popleft() #弹出左边的元素

q.rotate(2) #从右往左边移动2个位置
q.rotate(-1) #从左边往右边移动

#time模块
import time
print time.asctime()
print time.strftime("%Y-%m-%d") #将时间按设定的格式显示


