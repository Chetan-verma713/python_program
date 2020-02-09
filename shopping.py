n = []
while 1:
    c = input('Do you want to add any other thing? ')
    if c == 'yes':
        s = input("What? : ")
        n.append(s)
    else:
        break
print(n)
