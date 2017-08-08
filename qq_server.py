# coding: utf-8
from socket import *

# create a socket
server_socket = socket(AF_INET, SOCK_STREAM)

# create a bind
server_socket.bind(('127.0.0.1', 9001))

# listen socket
server_socket.listen(5)

while True:
	# make a new socket
	new_socket, client_addr = server_socket.accept()
	
	while True:
		recv_data = new_socket.recvfrom(1024)

		if len(recv_data) > 0:
			print recv_data
		else:
			break
		# what server to send
		send_data = raw_input('2server: ')
		new_socket.send(send_data)
	
	new_socket.close()

server_socket.close()
