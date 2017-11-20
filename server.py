import socket               # Import socket module
import time

print('Soy El servidor...')

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
print ('Esperando Conexion...')
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Me conecte al cliente.!!..', addr)
   print ('Enviando Mensaje.....')
   c.send(b"Soy un Mensaje")
   c.close()                # Close the connection