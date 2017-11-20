import socket               # Import socket module
import time

print ('Soy Un Cliente...')
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
msg = s.recv(1024)
print ('Mensaje recivido: ',msg)

time.sleep(20)
s.close                     # Close the socket when done