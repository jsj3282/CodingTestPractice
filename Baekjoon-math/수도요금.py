a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())
 
x_p = a * p
 
if p - c > 0:
    y_p = b + (p - c) * d
else:
    y_p = b
 
print(min(x_p, y_p))
