n = int(input())

c = 100
s = 100

for _ in range(n):
    a, b = map(int, input().split())

    if a < b:
        c -= b
    elif b < a:
        s -= a

print(c)
print(s)
