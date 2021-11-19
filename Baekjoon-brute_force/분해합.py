n = int(input())

res = 0

for i in range(1, n+1):
    a = list(map(int, str(i)))
    result = i + sum(a)
    if result == n:
        print(i)
        break
else:
    print(0)
