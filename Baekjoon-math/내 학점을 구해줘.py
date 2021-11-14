T = int(input())

for _ in range(T):
    n = int(input())
    c_s = 0
    g_s = 0
    for _ in range(n):
        c, g = input().split()
        c_s += int(c)
        g_s += float(g) * int(c)
    print(c_s, g_s / c_s)
