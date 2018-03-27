from socket import *

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('localhost',serverPort))
serverSocket.listen(1)

#the server is now set up to receive from the localhost and port 12000
print ('The server is ready to receive')

while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    #change the message to all upper case
    capitalizedSentence = sentence.upper()
    #send the message to the client that connected
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()
