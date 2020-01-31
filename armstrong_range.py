n = int(input("Enter a range "))
for j in range(1,n):
	s = 0
	j = str(j)
	pw = len(j)
	for i in j:
		s+= int(i)**pw
	if int(j)==s:
		print(j)
	else:
		continue
