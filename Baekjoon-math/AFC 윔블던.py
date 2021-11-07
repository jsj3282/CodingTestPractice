s, d = map(int, input().split())
 
if s - d < 0 or (s-d) % 2 != 0 :
    print(-1)
else:
    a = (s + d) // 2
    b = s - a
    print(max(a, b), min(a, b))
