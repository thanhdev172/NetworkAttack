import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(('localhost', 7))
s.listen(5)
client, address = s.accept()
while True:
	data = client.recv(2048)
	if(data):
		print("Received from client: %s" %data)
		client.send(data)
client.close()
