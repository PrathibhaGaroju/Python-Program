import socket

s = socket.socket()
print("Socket Successfully Created")


port = 40674

s.bind(('',port))
print("socket binded to %s" %(port))

s.listen(5)
print("socket is listening")


while True:

   c, addr = s.accept()
   print('Got connection from', addr)

   c.send(b'Thank You for connecting')

   c.close()
