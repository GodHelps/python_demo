'''multiThread 本实例中通过新建threading.Thread的子类和
直接使用threading.Thread创建线程介绍线程的简单使用.
'''
import threading
import time, random

class  MyThread(threading.Thread):
    "MyThread carry on the threading.Thread"

    def __init__(self,arg):
        "constructor"
        threading.Thread.__init__(self) #call the father constructor
        #init itself
        self.args=arg

    def run(self):
        "overide the father method,define whath you want"
        #run a test method
        res=self.test(self.args[0],self.args[1])# run 方法中不能直接将元组self.args-代替(self.args[0],self.args[1])使用
        print(self.name,"create by MyThread,the result is:",res)
        
    def test(self,x,y):
        "a test method,input two Integer,sleep'y'seconds return the Product"
        time.sleep(y)
        return(x*y)

def test(x,y):
    "a test method,input two Integer,sleep'y'seconds return the Product"
    time.sleep(y)
    res=x*y
    print("create by threading.Thread,the result is:",res)

def  main():
    try:
        threads=[] #define a empty threadlist
        nloop=range(2)
        loop_len=len(nloop)

        for i in range(loop_len):
            arg=(i,nloop[i])
            
            t1=threading.Thread(target=test,args=arg)# 可以将元组args-代替(self.args[0],self.args[1])使用
            t2=MyThread(arg)
            
            threads.append(t1)
            threads.append(t2)
    
        for i in range(len(threads)):
            threads[i].start()
            threads[i].join()

    except Exception as e:
        print(type(e),str(e))
        
if __name__=="__main__":
    main()
