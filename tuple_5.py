# Write a Python program to add an item in a tuple.
n = ()
while 1:
	item = input("Enter a item : ")	
	n += (item,)
	t = input("Do you want to add next one : ")
	if t.lower()=="no":
		break
print(n)
	
	
