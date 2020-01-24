a = input("Enter a string  ").split()
k = []
for i in a:
	b = a.count(i)
	if i not in k:
		print(i,":",b)
		k+=i
	
