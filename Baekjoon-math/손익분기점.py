a, b, c = map(int, input().split())
 
if c - b > 0:
    count = a // (c - b)
    print(count + 1)
else:
    print(-1)
