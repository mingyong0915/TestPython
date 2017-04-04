#!/usr/bin/env python  
# _*_ coding:utf-8 _*_

""" 
@version: v1.0 
@author: MingYong 
@license: Apache Licence  
@contact: 13760182207@163.com 
@site: http://blog.csdn.net/mingyong_blog 
@software: PyCharm 
@file: 005.py 
@time: 2017/4/4 9:16 
"""

# python的sys模块、os模块、fileinput模块
import sys
print sys.path
#
print sys.argv
# sys.exit([arg])
print sys.modules

#sys.platform :win32
print sys.platform
#sys.stdin
#sys.stdout
#sys.stderr


#os模块
import os

#os.environ 环境变量
print os.environ['PATH']  #E:\Program Files\Java\jdk1.8.0_112\bin;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;;C:\Perl\bin\;C:\Program Files (x86)\IDM Computer Solutions\UltraEdit;E:\Program Files (x86)\CTEX\UserData\miktex\bin;E:\Program Files (x86)\CTEX\MiKTeX\miktex\bin;E:\Program Files (x86)\CTEX\CTeX\ctex\bin;E:\Program Files (x86)\CTEX\CTeX\cct\bin;E:\Program Files (x86)\CTEX\CTeX\ty\bin;E:\Program Files (x86)\CTEX\Ghostscript\gs9.05\bin;E:\Program Files (x86)\CTEX\GSview\gsview;E:\Program Files (x86)\CTEX\WinEdt;C:\Users\ivy\AppData\Roaming\npm;E:\Program Files\Java\jdk1.8.0_112\bin;E:\Program Files\Java\jdk1.8.0_112\jre\bin;E:\apache-ant-1.9.7-bin\apache-ant-1.9.7\bin;E:\apache-maven-3.3.9-bin\apache-maven-3.3.9\bin
#os.system(commend) #执行命令
#os.system(r'C:\"Program Files (x86)"\"Mozilla Firefox"\firefox.exe') #因为Program Files (x86)有空格 要用双引号引起来
#os.startfile() #效果等同于os.system()
#os.startfile(r"\Program Files (x86)\Mozilla Firefox\firefox.exe")
#启动浏览器的专业方法 webbrowser.open()
import webbrowser
#webbrowser.open("www.baidu.com")

#os.sep  路劲分割符
print os.sep
#os.pathsep
print os.pathsep #输出：分号
#os.linesep 换行符
print "aaa"+os.linesep+"bbb"
#os.urandom(n)

#os.fileinput 文件输入模块
#fileinput.input()
#fileinput.filename()
#fileinput.lineno()
#fileinput.filelineno()
#fileinput.isstdin()
#fileinput.nextfile()
#fileinput.close()
