"# Echo client program"
import socket

try:
    HOST = '127.0.0.1'    # The remote host
    PORT = 18080              # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world') 
    data = s.recv(1024)
    #endstrs=""
    #s.sendall(endstrs.encode("utf-8","strict")) #默认关闭socket时会发送一个条空消息
    s.close()
    print('Received', repr(data.decode()))
except Exception as e:
    print(str(e))
