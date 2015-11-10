"Thread demo"#采用继承threading.Thread类,重写run方法定制线程执行方法.
from multiprocessing import Pool
import threading
import time, random
import os

seperation=os.linesep

class Counter:
    def __init__(self):
        self.lock = threading.Lock()

        self.value = 0
    def increment(self):
        self.lock.acquire() # critical section
        self.value = value = self.value + 1
        self.lock.release()
        return value
    
counter = Counter()

#继承Thread 类, 重写run 方法, 就可以创建一个新的线程或多个实例,然后调用 start 方法启动
class Worker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)#显示的调用基类的init方法
        
    def run(self): #重写run 方法,自定义线程运行方式 
        for i in range(2):
        # pretend we're doing something that takes 10?00 ms
            value = counter.increment() # increment global counter
            time.sleep(random.randint(10, 100) / 1000.0)
            self.lock = threading.Lock()
            self.lock.acquire()
            info=self.getName()+"-- task finished:"+str(value)+seperation
            print(info)
            self.lock.release()
#
# try it
for i in range(10):
    Worker().start() # start a worker
