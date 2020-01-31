n = input("Enter a no. ")
pw = len(n)
s = 0
for i in n:
	s+= int(i)**pw
if int(n)==s:
	print("No. is armstrong ")
else:
	print("Armstrong not ")
