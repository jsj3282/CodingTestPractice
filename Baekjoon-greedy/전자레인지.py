t = int(input())
 
a = t // 300
b = t % 300
t = b
 
b = t // 60
c = t % 60
t = c
 
c = t // 10
t = t % 10
 
if t != 0:
    print(-1)
else:
    print(a, b, c)
