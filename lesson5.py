#1
n = int(raw_input("Enter n: "))
s = 0
for i in range(1, n + 1):
	s = s + i
print("S = {}".format(s))
#2
s1 = 0
for i in range(1, n + 1):
	s1 = s1 + (2*i - 1)
print("S1 = {}".format(s1))
#3
s2 = 0
for i in range(1, n + 1):
	s2 = s2 + 2*i
print("S2 = {}".format(s2))
#4
s3 = 0
for i in range(1, n + 1):
	s3 = s3 + i**2
print("S3 = {}".format(s3))
#5
s4 = 0
for i in range(0, n):
	s4 = s4 + (1.0/2)**i
print("S4 = {}".format(s4))




