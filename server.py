import socket
import sys
import time

s = socket.socket()
host = 'localhost'
print(" server will start on host : ", host)
port = 8080
s.bind((host,port))
print("")
print(" Server done binding to host and port successfully")
print("")
print("Server is waiting for incoming connections")
print("")
s.listen(1)
conn, addr = s.accept()
print(addr, " Has connected to the server and is now online ...")
print("")
while 1:
	message = raw_input("enter your message >>")
	message = message.encode()
	conn.send(message)
	print("message has been sent...")
	print("")
	incoming_message = conn.recv(1024)
	incoming_message = incoming_message.decode()
	incoming_message = str(incoming_message)
	print(" Client says >>")
	print(incoming_message)
	print("")

