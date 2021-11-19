t = int(input())

for _ in range(t):
    d, n, s, p = map(int, input().split())
    p_t = d + n * p
    s_t = n * s
    if p_t > s_t:
        print("do not parallelize")
    elif s_t > p_t:
        print("parallelize")
    else:
        print("does not matter")
