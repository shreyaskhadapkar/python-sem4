import socket
f = open("Important.txt","w")              #Creating a file
f.write("This is python experiment no.6.3. In this experiment server will search for a file asked by client"+
        " and if found" + "then download it for server and display for client")
f.close()
host="localhost"
port=8787
s=socket.socket()  
s.bind((host,port))
s.listen(1)
h,d = s.accept() 
print("Client is online Now")
fname = h.recv(1024)
fname = str(fname.decode())
print("Client want " + fname  + "file")
try:
    f = open(fname,"rb")
    matter = f.read()
    h.send(matter)
    print(fname + " file sent to client")
    f.close()
except FileNotFoundError:
    h.send(b"Your file not found Sorry")
s.close()                              
