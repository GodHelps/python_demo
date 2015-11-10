"product-consumer.py"#生产者－消费者问题,实现中使用了Queue 对象和随机地生产（和消耗）货物的方式。生产者和消费者相互独立
#并且并发地运行

import random
from time import sleep
from queue import Queue
import threading

import os
seperation=os.linesep

class product(threading.Thread):
    global rlock
    def __init__(self,arg,name):
        threading.Thread.__init__(self)
        self.name=name
        self.args=arg

    def run(self):
        "overide father method"
        self.writer(self.args[0],self.args[1])
        
    def writeQ(self,que,loops):
        "in queue method"
        for i in range(loops):
            rlock.acquire()
            print(('producing object for Q...'))    
            que.put('xxx')
            print("Queue size now:", (str(que.qsize())+seperation))
            rlock.release()
            sleep(random.randint(1, 3))

    def writer(self,que, loops):
        "product method"    
        self.writeQ(que,loops)
        


class consumer(threading.Thread):
    def __init__(self,arg,name):
        threading.Thread.__init__(self)
        #self.lock=rlock
        self.name=name
        self.args=arg

    def run(self):
        "overide father method"
        self.reader(self.args[0],self.args[1])

    def readQ(self,que,loops):
        "out queue method"
        for i in range(loops):
            rlock.acquire()
            val = que.get()
            print('consumed object from Q...','Queue size now:',(str(que.qsize())+seperation))
            rlock.release()
            sleep(random.randint(2, 5))

    def reader(self,que,loops):
        "custom method"
        self.readQ(que,loops)
            

#define global veriable
funcs = [product, consumer] 
nfuncs = range(len(funcs))
rlock=threading.RLock()
 
def main():
    "Test main method "
    nloops = random.randint(2, 5)
    q = Queue(32)
    threads = []
    for i in nfuncs:
        arg=(q, nloops)
        
        #t = threading.Thread(target=funcs[i], args=(q, nloops),name=funcs[i].__name__)
        t=funcs[i](arg,funcs[i].__name__)
        print("has create a thread: ",funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()
    for i in nfuncs:
        threads[i].join()

    print('all DONE')
if __name__ == '__main__':
    main()
