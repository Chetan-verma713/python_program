n = int(input("Enter a no. : "))
r = 0
while n!=0:
    c = n%10
    r += c
    n //= 10
print("Total is : ",r)
    
