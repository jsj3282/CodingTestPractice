n, h, v = map(int, input().split())
 
p1 = 4 * h * v
p2 = 4 * (n - v) * h
p3 = 4 * (n - h) * v
p4 = 4 * (n - h) * (n - v)
 
print(max(p1, p2, p3, p4))
