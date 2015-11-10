"TCPsocket client demo"
"server:tssockserver.py"
"client:tssockclient.py"
import socket
import time

def serverInit(ip,port):
    "Init socket server"
    tcpCliSock=None #define a none socket
    try:
        Host=ip
        Port=port
        BufSize=1024
        Addr=(Host,Port)
        tcpCliSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcpCliSock.connect(Addr)
        while True:
            inputs=input("enter you want<enter[.] quit>:")
            if inputs!=".":
                tcpCliSock.send(inputs.encode("utf-8","strict"))
                data = tcpCliSock.recv(BufSize)
                if not data:
                    print("对方断开连接")
                    break
                print("Recv:"+data.decode())
            else:
                break
        tcpCliSock.close()

    except BaseException as e:
        if  tcpCliSock:
            tcpCliSock.close()
        if isinstance(e,(KeyboardInterrupt ,SystemExit,EOFError)):
             print("Error Message:",type(e),str(e))

def main():
    "Test method"
    ip="127.0.0.1"#input(please input ip)
    port=18080    #input(please input port)
    serverInit(ip,port)

if __name__=="__main__":
    main()
