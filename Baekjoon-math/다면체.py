T = int(input())

for _ in range(T):
    v, e = map(int, input().split())
    s = 2 - (v - e)
    print(s)
