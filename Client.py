import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port =1080

# connect to the server on local computer
s.connect(('', port))

# receive data from the server
print (s.recv(1024))
# close the connection
s.close()