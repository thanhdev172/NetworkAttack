import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9999))
s.listen(5)

while 1:
	cli, (remhost, remport) = s.accept()
	print("Received connection form", remhost)
	cli.send("Hello {}\n".format(remhost))
	cli.close()
