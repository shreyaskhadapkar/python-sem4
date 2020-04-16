import socket
host="localhost"
port=8787
socket = socket.socket()
socket.connect((host,port)) 
Name=input("Enter Filename: ")
socket.send(Name.encode())
matter = socket.recv(2048)
print(matter.decode())
socket.close()    
