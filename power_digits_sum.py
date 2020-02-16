t = int(input())
while t>0:
  n = int(input())
  n = 2**n
  r = 0
  s = 0
  while n!=0:
    r = n%10
    s += r
    n = n // 10
  print(s)
  t -= 1
