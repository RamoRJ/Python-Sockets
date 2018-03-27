from socket import *
#set server to local host
serverName ='localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
#write a message to send to the serer
sentence = input('Input lowercase sentence: ')
bytes_message = bytes(sentence, 'utf-8')

#send a message to the server
clientSocket.send(bytes_message)
modifiedSentence = clientSocket.recv(1024)

#decode the message to get rid of the leading b
newSentence = modifiedSentence.decode('utf-8')
print ('From Server:', newSentence)

clientSocket.close()
