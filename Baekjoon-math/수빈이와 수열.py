n = int(input())
b = list(map(int, input().split()))
a = []

sum = 0
for i in range(n):
    a.append(b[i] * (i + 1) - sum)
    sum += a[i]

for i in a:
    print(i, end=" ")
