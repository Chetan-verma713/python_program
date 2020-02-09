n1 = int(input("Enter 1st side : "))
n2 = int(input("Enter 2nd side : "))
n3 = int(input("Enter 3rd side : "))
if (n1 == (n2**2 + n3**2)**0.5):
    print("Perfect right angle triangle ")
elif (n2 == (n1**2 + n3**2)**0.5):
    print("Perfect right angle triangle ")
elif (n3 == (n1**2 + n2**2)**0.5):
    print("Perfect right angle triangle ")
else:
    print("Not a perfect right angle triangle ")
