a = []
b = []
T = int(input())
 
for _ in range(T):
    num1, num2 = map(int, input().split())
    a.append(num1)
    b.append(num2)
 
for i in range(T):
    base = a[i] % 10
 
    if base == 0:
      print(10)
 
    elif base in [1, 5, 6]:
      print(base)
  
    elif base in [4, 9]:
      if b[i] % 2 == 0:
        print(base ** 2 % 10)
      else:
        print(base)
  
    else:
      if b[i] % 4 == 0:
        print(base ** 4 % 10)
      else:
        print(base ** (b[i] % 4) % 10)
