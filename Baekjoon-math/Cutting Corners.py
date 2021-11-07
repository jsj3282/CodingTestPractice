import math
 
w, h = map(int, input().split())
d = math.sqrt(w ** 2 + h ** 2)
 
print(w + h - d)
