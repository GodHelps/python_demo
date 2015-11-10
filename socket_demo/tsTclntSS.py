"创建一个时间戳TCP 客户端，它知道如何与socketserver 里StreamRequestHandler 对象进行通讯"
"server:tsTservSS.py"
"client:tsTclntSS.py"

import socket
import os

HOST = 'localhost'
PORT = 18080
BUFSIZ = 1024
ADDR = (HOST, PORT)
lineseperate=os.linesep

def Tcpclient():
    "client method"
    while True:
        tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpCliSock.connect(ADDR)
        inputs=input("enter you want<enter[.] quit>:")
        if inputs!=".":
            tcpCliSock.send((inputs+lineseperate).encode("utf-8","strict"))
            data = tcpCliSock.recv(BUFSIZ)
            if not data:
                print("对方断开连接")
                break
           
            else:
                print("Recv:"+data.decode())
    tcpCliSock.close()
def main():
    "Test method"
    try:
        Tcpclient()  
    except BaseException as e:
        if isinstance(e,(KeyboardInterrupt ,SystemExit,EOFError)):
            print("Error Message:",type(e),str(e))

if __name__=="__main__":
    main()
