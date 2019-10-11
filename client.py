import socket
import sys


tcpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = sys.argv[1]
port = int(sys.argv[2])
obj = sys.argv[3]
# HTTP GET method header information
get_str = '''GET {} HTTP/1.1
Host: {}
User-Agent: MyPythonClient
Accept: */*

'''
try:
    print('try to connect server', host)
    tcpClientSocket.connect((host, port))
    send_str = get_str.format('/'+obj, host+':'+str(port))
    # print(send_str)
    tcpClientSocket.send(send_str.encode())  # do a GET method
    data = tcpClientSocket.recv(2048)
    if data:
        print(data)
    tcpClientSocket.close()
except:
    pass
