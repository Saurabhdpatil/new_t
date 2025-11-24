//server.py
import socket
import struct

server = socket.socket()
server.bind(("localhost", 6666))
server.listen(1)

print("Server started... Waiting for client...")
conn, addr = server.accept()
print("Client connected:", addr)

data = conn.recv(8)
a, b = struct.unpack('ii', data)

print("Sum =", a + b)

conn.close()
server.close()


//client.py

import socket
import struct

s = socket.socket()
s.connect(("localhost", 6666))

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

s.send(struct.pack('ii', a, b))
s.close()


// input 
Enter 1st number: 10
Enter 2nd number: 15

