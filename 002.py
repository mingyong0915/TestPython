#!/usr/bin/env python  
# _*_ coding:utf-8 _*_

""" 
@version: v1.0 
@author: MingYong 
@license: Apache Licence  
@contact: 13760182207@163.com 
@site: http://blog.csdn.net/mingyong_blog 
@software: PyCharm 
@file: 002.py 
@time: 2017/4/2 23:13 
"""

#python 魔法方法
# __init__: 构造方法
# __del__: 析构方法
#  __len__(self) : 返回元素数量
# __getitem__(self, key):返回键对应的值
# __setitem__(self, key, value):按照方式存储和key相关的value
# __delitem__(self, key):删除元素


class FooBar:
    def __init__(self, value=42):#构造方法
        self.somevar = value


f = FooBar()
print f.somevar

# 重写方法；对继承的方法如果觉得不合用，可以用重写的方法对父类的方法进行覆盖

__metaclass__ = type


class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print "Aaaah..."
            self.hungry = False
        else:
            print "No,thanks!"


class SongBird(Bird):
    def __init__(self):
        #Bird.__init__(self)#调用未绑定的超类构造方法
        super(SongBird, self).__init__()#新式类的调用父类构造方法
        self.sound = "Qssdd"
    def sing(self):
        print self.sound
sb = SongBird()
sb.sing()
sb.eat()

def checkIndex(key):
    if not isinstance(key, (int,long)):raise TypeError
    if key < 0:raise IndexError


class ArithmeticSequnce:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        checkIndex(key)
        try:return self.changed[key]
        except KeyError:
            return self.start+key*self.step

    def __setitem__(self, key, value):
        checkIndex(key)
        self.change[key] = value

s = ArithmeticSequnce(1,2)
print s[4]

class CounterList(list):
    def __init__(self, *args):
        super(CounterList, self).__init__(*args)
        self.counter=0

    def __getitem__(self, index):
        self.counter+=1
        return super(CounterList,self).__getitem__(index)

c = CounterList(range(10))
print c[4]
print c.counter

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height
    size = property(getSize, setSize)
r = Rectangle()
r.width = 10
r.height = 100
print r.size
r.size = (200,100)
print r.width
print r.height


class Rectangle2:
    def __init__(self):
        self.width = 0
        self.height = 0
    def __setattr__(self, key, value):
        if key == "size":
            self.width, self.height = value
        else:
            self.__dict__[key] = value
    def __getattr__(self, item):
        if item == "size":
            return self.width, self.height
        else:
            raise AttributeError

r2 = Rectangle2()
r2.size = (2,2)
print r2.width
print r2.height