#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time
import os

thread_num = os.getenv('THREADNUM', "10")
delay = os.getenv('DELAY', "0")

statistic = {
    'total_log_num': 0,
    'start_time': time.time()
}

class myThread (threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
    def run(self):
        print "Starting " + self.name
        print_time(self.name, self.delay)

def print_time(threadName, delay):
    while True:
        time.sleep(delay)
        statistic['total_log_num'] += 1
        print "{} runs cmd print '{}' for {} times" .format(threadName, time.ctime(time.time()), statistic['total_log_num'])
        # f = open("logtesting", 'a')
        # f.write(time.ctime(time.time()) + ' runs ' + str(sum) + ' times\n')

        diff = time.time() - statistic["start_time"]
        print 'programme runs {}s'.format(diff)
        log_num_per_second = statistic['total_log_num'] / diff
        print 'log num per second is {}'.format(log_num_per_second)

print thread_num
for i in range(int(thread_num)):
    myThread("Thread-{}".format(i), int(delay)).start()

