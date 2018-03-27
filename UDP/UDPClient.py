from socket import *

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET,SOCK_DGRAM)

message = input('input lowercase message to server:')

#need to encode the str object into a bytes object for python 3
bytes_message = bytes(message, 'utf-8')

#send the messages to the server using the name and port of the server
clientSocket.sendto(bytes_message, (serverName,serverPort))
messageFromServer,serverAddress = clientSocket.recvfrom(2048)

print (messageFromServer)
clientSocket.close()
