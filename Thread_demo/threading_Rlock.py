'''本实例中简单介绍threading.Rlock的用法,
threading.Rlock与threading.Lock的不同点在于threading.Rlock的实例可以多次调用成对
的acquire()和release()方法，而threading.Lock的实例则不行，如果acquire()和release()方法
不进行一对一调用将会出现死锁。
'''
import threading
import time

mylock = threading.RLock()  
num=0  
   
class myThread(threading.Thread):  
    def __init__(self, name):  
        threading.Thread.__init__(self)  
        self.t_name = name  
          
    def run(self):  
        global num  
        while True:  
            mylock.acquire()  
            print('Thread',self.t_name, 'locked Number:',num)  
            if num>=4:  
                mylock.release()  
                #print('\nThread',self.t_name," released, Number don't changed:",num)  
                break  
            num+=1  
            print ('Thread',self.t_name,'released, Number changed:', num)  
            mylock.release()
            time.sleep(1)
              
def test():  
    thread1 = myThread('A')  
    thread2 = myThread('B')  
    thread1.start()  
    thread2.start()
    for i in range(2):
        thread1.join()
        thread2.join()
    print('\n All Thread end', 'Number :',num)
        
   
if __name__== '__main__':  
    test()  
