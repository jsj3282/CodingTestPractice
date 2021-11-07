import math
 
k, n, m = map(int, input().split())
 
if m - (k * n) < 0:
    print(abs(m - (k * n)))
else:
    print(0)
