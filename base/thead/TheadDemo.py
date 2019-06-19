#!/usr/bin/python
#-*-coding:utf-8-*-

import thread
import time

# 为线程定义一个函数
def print_time(name,delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (name, time.ctime(time.time()))

# 创建两个线程
try:
    thread.start_new_thread(print_time, ("Thead-1", 2))
    thread.start_new_thread(print_time, ("Thead-2", 4))
except:
    print "Error: unable to start thread"

while 1:
    pass

print "End."