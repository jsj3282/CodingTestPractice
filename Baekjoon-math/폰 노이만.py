p = int(input())

for _ in range(p):
    n, d, a, b, f = map(float, input().split())
    print(int(n), d / (a + b) * f)
