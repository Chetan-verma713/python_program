a = input("Enter a string  ")
for i in a:
	b = a.count(i)
	if i==i+1:
		continue
	print(i,b)
