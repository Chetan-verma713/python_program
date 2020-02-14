ls = [1, 2, 3, 4, 5, (1,), 6]
c = 0
for i in ls :
	if type(i) != tuple:
		c += 1
	else:
		break
print(c)
