# coding: utf-8
from socket import *

# create a socket 
client_socket = socket(AF_INET, SOCK_STREAM)

# create a connection
client_socket.connect(('127.0.0.1', 9001))

# send and receive
while True:
	# what you want to say
	send_data = raw_input('2json_client：')

	if len(send_data) > 0:
		client_socket.send('2json_client: ' + send_data)
	else:
		break
	
	# get information
	recv_data = client_socket.recvfrom(1024)
	print recv_data

# close socket
client_socket.close()
