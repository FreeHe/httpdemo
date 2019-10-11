# import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM) # create a server socket

try:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
except:
    HOST = ''
    PORT = 6789

SUCCESS_RESPONSE_HEADER = '''HTTP/1.1 200 OK
Server: MyPythonServer
Content-Type: text/html
Accept-Ranges: bytes
Connection: close

'''
FAILD_RESPONSE_HEADER = '''HTTP/1.1 404 Not Found
Server: MyPythonServer
Content-Type: text/html
Accept-Ranges: bytes
Connection: close

<h1>404 Not Found</h1>
'''
# Prepare a server socket   
serverSocket.bind((HOST, PORT))
print("server bind to ", HOST, PORT)
while True:
    serverSocket.listen(1)  # the Server listen to the port, ready to accept the connection of client
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # if client connect to the server, we get the
    print("Connection from ", addr)                 # socket of client and the address(a tuple consist
    try:                                            # of IP and port of client) of client
        message = connectionSocket.recv(1023).decode()  # when client do a GET request,we receive the message,
                                                        # you can see the format of message clearly by printing it.
        filename = message.split()[1]                   # get the filename the client requested
        if filename == "/hello.html":
            f = open(filename[1:])
            outputdata = SUCCESS_RESPONSE_HEADER + f.read() + "\r\n"  # http data consist of header and body(file text)
            f.close()
            connectionSocket.sendall(outputdata.encode())  # send http data to client
            connectionSocket.close()  # close connection
        else:  # if the file that client requested is not exist,we return 404 Not Found
            outputdata = FAILD_RESPONSE_HEADER
            connectionSocket.sendall(outputdata.encode())
            # Close client socket
            connectionSocket.close()
    except Exception as e:
        connectionSocket.close()

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
