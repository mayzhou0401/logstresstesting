#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time
import os

thread_num = os.getenv('THREADNUM', 10)

class myThread (threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
    def run(self):
        print "Starting " + self.name
        print_time(self.name, self.delay)

def print_time(threadName, delay):
    sum =0
    while True:
        time.sleep(delay)
        sum = sum + 1
        print "{} runs cmd print '{}' {} times" .format(threadName, time.ctime(time.time()), sum)
        # f = open("logtesting", 'a')
        # f.write(time.ctime(time.time()) + ' runs ' + str(sum) + ' times\n')

print thread_num
for i in thread_num:
    myThread("Thread-{}".format(i), 0).start()

