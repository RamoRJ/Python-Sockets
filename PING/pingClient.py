# client side of the ping socket program
import time
import sys
from socket import *

pings = 1
rec = 0
lost = 0
min = 0
max = 0
total = 0

#UDP socket creation
clientSocket = socket(AF_INET, SOCK_DGRAM)

#timeout at 1 second
clientSocket.settimeout(1)

#set the host and the message
host = "127.0.0.1"
message = ('ping (%s)' % host)
size = sys.getsizeof(message)
print("pinging %(host)s with %(size)d bytes of data: \n" % {'host': host, 'size': size})

#set message to bytes object
bytes_message = bytes(message, 'utf-8')

addr = (host, 12000)

#send 10 pings
while pings < 11:  


    #Send ping
    start = time.time()
    clientSocket.sendto(bytes_message, addr) 

    #if we get something from the server - display information.
    try:
        data, server = clientSocket.recvfrom(1024)
        newData = data.decode('utf-8')
        end = time.time()
        elapsed = end - start
        print(str(pings) + " Reply from " + str(host) + ":\ntime=" + str(elapsed) +"ms\n" ) #set all values to string objects (just to make sure)      
        rec = rec + 1
        if min > elapsed:
            min = elapsed

        if max < elapsed:
            max = elapsed
        total = total + elapsed


    #if nothing from server - time out message  
    except timeout:
        print(str(pings) + " Request timed out \n")
        lost = lost + 1

    pings = pings + 1

percent = lost*100/(pings -1)
average = total/rec

print("Ping statistics for " + host + ":")
print("Packets: Sent = " + str(pings - 1) + ", Received = " + str(rec) + ", Lost = " + str(lost) + " (" + str(percent) + "% loss) \n")
print("Approximate round trip times in milli-seconds:")
print("Minimum = " + str(min) + "ms\nMaximum = " + str(max) + "ms\nAverage = " + str(average) + "ms")