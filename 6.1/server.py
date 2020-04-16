import socket
host="localhost"
port=6789

#tcp socket connection
socketTest = socket.socket()

#binding socket with host and port
socketTest.bind((host,port))
socketTest.listen(1)
d,destination=socketTest.accept()
print("CLIENT IS ONLINE")

#Establishing connection between client and server
while True:
    a=d.recv(1024)
    if not a:
        break
    print("Client is saying:",a.decode())
    t = input("REPLY: ")
    d.send(t.encode())

#Closing that connection
d.close()
