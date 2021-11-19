n, m = map(int, input().split())
li = map(int, input().split())
res = 1
for i in li:
    res *= i
print(res % m)
