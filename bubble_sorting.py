ls = [2, 4, 5, 3, 6, 1]
n = len(ls)
for j in range(n):
    for i in range(0,n-j-1):
        if i>(i+1):
            ls[i],ls[i+1] = ls[i+1],ls[i]
for j in range(n):
    print(ls)   
