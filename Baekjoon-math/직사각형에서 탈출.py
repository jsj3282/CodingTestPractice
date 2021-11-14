x, y, w, h = map(int, input().split())
 
print(min((w - x), (y - 0), (h - y), (x - 0)))
