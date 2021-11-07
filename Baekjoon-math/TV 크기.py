import math
 
a, b, c = map(int, input().split())
 
x = 0
x = math.sqrt(a ** 2 / (b ** 2 + c ** 2))
 
# print(x)
height = math.floor(b * x)
width = math.floor(c * x)
 
print(height, width)
