import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto("Hi there\n", ('127.0.0.1', 9999))
data, (a, p) = s.recvfrom(1024)
print(data)

s.close()
