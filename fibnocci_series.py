n = int(input("Enter a no. : "))
t1 = 0
t2 = 1
nt = 0
for i in range(n+1):
    print(t1)
    nt = t1 + t2
    t1 = t2
    t2 = nt
    
