a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())
 
t1 = (T - 30) * x * 21 if T >= 30 else 0
t2 = (T - 45) * y * 21 if T >= 45 else 0
 
ans1 = a + t1
ans2 = b + t2
 
print(ans1, ans2)
