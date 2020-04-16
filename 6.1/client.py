import socket
host="localhost"
port=6789

#tcp socket connection
h = socket.socket()

#connecting socket with host and port of server
h.connect((host,port))
message = input("To Server: ")

#Establishing connection between client and server
while message!="end":
    h.send(message.encode())
    reply=h.recv(1024)
    reply=reply.decode()
    print("Server : "+reply)
    message = input("To Server : ")
h.close()                                      
