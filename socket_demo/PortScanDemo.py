"socket_port scan demo"#服务器端口扫描Demo

import socket
import os
import threading
import time

#define globle variable
host="www.baidu.com"
Port=80
addressfaimly=socket.AF_INET
socktype=socket.SOCK_STREAM
scan_destport=100
#lock = threading.Lock() #define thread lock
threads= []
tcpClientScok=socket.socket(addressfaimly,socktype)
ip=socket.gethostbyname(host)

def portScan():
    try:
        
        #lock.acquire()
        '''td=threading.Thread(target=scan,args=([80]))
        td.start()'''
        for eachport in range(70,80,1):
            td=threading.Thread(target=scan,args=([eachport]))
            
            threads.append(td)

        print("start scan....")    
        for i in range(10): # start threads
            threads[i].start()

        for i in range(10):
            threads[i].join() #threads to finish
         
        print ('all DONE at:',time.ctime())'''
    except BaseException as e:
        print("Error message:",type(e),str(e))
        
def scan(pr):
    "the method to scan"
    try:
        tcpClientScok.connect((ip,pr))
        print("{0}ok".format(pr)+os.linesep)
    except:
        pass

def main():
    try:
        portScan()
    except BaseException as e:
        print("Error message:",type(e),str(e),os.linesep)

if __name__=="__main__":
    main()



        
        
