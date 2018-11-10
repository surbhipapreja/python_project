import socket
import sys
import time

s = socket.socket()
host = input("Please enter the hostname of the server : ")
port = 8080
s.connect((host,port))
print("Connected to chat server")
while 1:
	incoming_message = s.recv(1024)
	incoming_message = incoming_message.decode()
	incoming_message = str(incoming_message)
	print("Server says >>")
	print(incoming_message)
	print("")
	message = raw_input("Enter your message")
	message = message.encode()
	s.send(message)
	print("message has been sent...")
	print("")