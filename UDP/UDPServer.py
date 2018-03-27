from socket import *

serverPort = 12000

#set the server to a localhost
severSocket = socket(AF_INET,SOCK_DGRAM)
severSocket.bind(('127.0.0.1',serverPort))

print ('The server is ready to receive')

#get the message from the client and turn it into upper case with upper()
while True:
    message,clientAddress = severSocket.recvfrom(2048)
    modifiedMessage = message.upper()
    severSocket.sendto(modifiedMessage, clientAddress)
