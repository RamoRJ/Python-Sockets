# client side of the ping socket program
import time
from socket import *

pings = 1

#send 10 pings
while pings < 11:  

    #UDP socket creation
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    #timeout at 1 second
    clientSocket.settimeout(1)

    #Ping server
    message = 'test'

    #set message to bytes object
    bytes_message = bytes(message, 'utf-8')

    addr = ("127.0.0.1", 12000)

    #Send ping
    start = time.time()
    clientSocket.sendto(bytes_message, addr) 

    #if we get something from the server - display it.
    try:
        data, server = clientSocket.recvfrom(1024)
        newData = data.decode('utf-8')
        end = time.time()
        elapsed = end - start
        print(str(newData) + " " + str(pings) + " "+ str(elapsed) )       

    #if nothing from server - time out message  
    except timeout:
        print('REQUEST TIMED OUT')

    pings = pings + 1