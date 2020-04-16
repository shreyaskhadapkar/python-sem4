import socket 
host="localhost"
port=6789
h = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    i = input("To Server:")
    h.sendto(bytearray(i,"utf-8"), (host, port))
    s= h.recvfrom(1024)
    print("From Server: %s"%(s[0]))
h.close()                     
