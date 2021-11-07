import math
 
h, w = map(int, input().split())
 
a, b = max(h, w), min(h, w)
 
side1 = a / 3 if a / 3 <= b else b
side2 = b / 2
print(max(side1, side2))
