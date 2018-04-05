from socket import *

#create UDP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

#assign IP address and port to socket
serverSocket.bind(('', 12000))
serverSocket.listen(1)

while True:

    print('The HTTP server is ready to receive')
    #accept connections from the outside
    connectionSocket, addr = serverSocket.accept()

    try:
        #receive the request for an html page
        message = connectionSocket.recv(1024).decode()
        
        #set filename to the html page
        filename = message.split()[1]

        #open the file in the HTTP socket
        f = open(filename[1:])
        
        #read the file it opens (if it does)
        outputdata = f.read()

        
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        #if file opens, send file to webpage
        for i in range(0, len(outputdata)): 

            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

 

    except IOError:

        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())

        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())

        connectionSocket.close()