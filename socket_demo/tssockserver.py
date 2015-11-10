"TCPsocket server demo"
"server:tssockserver.py"
"client:tssockclient.py"
import socket
import time

def serverInit(ip,port):
    "Init socket server"
    try:
        Host=ip
        Port=port
        BufSize=1024
        Addr=(Host,Port)
        tcpSerSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcpSerSock.bind(Addr)
        tcpSerSock.listen(1)
        while True:
            print ('waiting for connection...')
            tcpCliSock, addr = tcpSerSock.accept()
            print('...connected from:', addr)
            while True:
                data = tcpCliSock.recv(BufSize)
                if not data:
                    print("对方断开连接")
                    break
                #print('Message from:', addr)
                print('Message from:', addr,data.decode())
                inputs=input("enter you want<enter[.] disconnect>:")
                if inputs!=".":
                    tcpCliSock.sendall(inputs.encode("utf-8","strict"))
                else:
                    tcpCliSock.close()
                    break
        tcpSerSock.close()

    except Exception as e:
            print(str(e))

def main():
    "Test method"
    ip="127.0.0.1"#input(please input ip)
    port=18080    #input(please input port)
    serverInit(ip,port)

if __name__=="__main__":
    main()
