import socket
host="localhost"
port=6789
socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket.bind((host,port))
print("CLIENT IS ONLINE")
while True:
    r= socket.recvfrom(1024)
    print("From Client: %s" %(r[0]))
    a = input("To Client:")
    socket.sendto(bytearray(a,"utf-8"), r[1])

socket.close()
