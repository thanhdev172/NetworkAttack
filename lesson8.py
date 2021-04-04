def findMax(list = []):
	max = -9999999999
	for x in list:
		if x > max:
			max = x
	return max
list = [2, 55, 99, 2, -2, 12]
print("Max: {}".format(findMax(list)))
