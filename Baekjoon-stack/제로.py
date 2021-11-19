k = int(input())
res = [0]

for i in range(k):
    n = int(input())
    if n == 0:
        res.pop()
    else:
        res.append(n)

print(sum(res))
