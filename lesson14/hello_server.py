import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 9999))

while 1:
	data, (a, p) = s.recvfrom(1024)
	print("Received data from", a)
	s.sendto("Hello %s\n" %a, (a, p))
