import math
 
a1, p1 = map(int, input().split())
r1, p2 = map(int, input().split())
 
v1 = a1 / p1
v2 = (math.pi * r1 ** 2) / p2
 
if v1 > v2:
    print("Slice of pizza")
else:
    print("Whole pizza")
