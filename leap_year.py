# program to check leap year.
n = int(input("Enter a year : "))
c = 0
if n%4==0:
    if n%100==0:
        if n%400==0:
            print("Year is a leap year ")
        else :
            print("Year is not a leap year")
    else:
        print("Year is a leap year")
else:
    print("Year is not a leap year")
