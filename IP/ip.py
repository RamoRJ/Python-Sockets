import socket

#ask for a site to find the ip address of
site = input('Input the URL of a website: ')
# get the ip address of the site and print it.
ip = socket.gethostbyname(site)
print(ip)

#ask for an ip address to find if it's v4 or v6
address = input('Input an IP address: ')
#find if it's v4 or v6
try:
    socket.inet_aton(address)
    print("This is an IPv4 address.")
except OSError:
    try:
        socket.inet_pton(socket.AF_INET6, address)
        print("This is an IPv6 address.")
    except OSError:
        print("That is not a valid IP address.")

#print out IP address allocated by DHCP for the host running Python
print ('')
print ('The following is the IP allocated by the DHCP: ')
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80)) #Google DNS and port
print(s.getsockname()[0])
s.close()
