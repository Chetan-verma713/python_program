l = [1, 2, 9, 8, 11, 13, 14, 17]
sl = list()
for i in l:
	c = 0
	
	for j in range(2,i):
		if i==1:
			c += 1
		if i%j==0:
			c += 1
	if c==0:
		sl.append(i)
print(sl)
	
