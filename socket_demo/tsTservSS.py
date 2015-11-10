"使用SocketServer 里的TCPServer 和StreamRequestHandler 类创建一个时间戳TCP 服务器"
"server:tsTservSS.py"
"client:tsTclntSS.py"

import socket
from socketserver import (TCPServer as TCP,
StreamRequestHandler as SRH,BaseRequestHandler as BRH)

from time import ctime
import os
import sys

lineseperate=os.linesep
HOST = ''
PORT = 18080
ADDR = (HOST, PORT)

class MyStreamRequestHandler(SRH):
    def handle(self):
        try:
            sys.exit()
            print('...connected from:', self.client_address)
            self.data=self.rfile.readline()
            print(self.data.decode()) #display the message recv
            #self.rfile like the file handle 但不可以迭代处理 ，不能向文件对象一样关闭。这需要研究
            #for eachline in handle: 
                #print(eachline.decode())
            print("self.rfile type:",type(self.rfile))
            # send the message
            data="message has been recvied"
            self.wfile.write(bytes(data +lineseperate, "utf-8"))

            '''
            # we can now use e.g. readline() instead of raw recv() calls
            #官方示例
            self.data = self.rfile.readline().strip()
            print("{} wrote:".format(self.client_address[0]))
            print(self.data.decode())
            print("self.rfile type:",type(self.rfile))
            
            # Likewise, self.wfile is a file-like object used to write back
            # to the client
            self.wfile.write(bytes("hello" +lineseperate, "utf-8"))
            '''
                
        except BaseException as e:
            print("Error Message:",type(e),str(e))
class MyBaseRequestHandler(BRH):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print("self.data type:",type(self.data))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

      

def main():
    "Test method"
    try:
        tcpServ = TCP(ADDR, MyStreamRequestHandler)
        print ('waiting for connection...')
        tcpServ.serve_forever()
    except BaseException as e:
        if  isinstance(e,(KeyboardInterrupt ,SystemExit,EOFError)):
            print(type(e),"操作成功,程序已退出")
        else:
            print("Error Message:",type(e),str(e))


if __name__=="__main__":
    main()
