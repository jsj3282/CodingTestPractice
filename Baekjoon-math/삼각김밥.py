x, y = map(int, input().split())

price1 = (1000 / y) * x

n = int(input())

kimbop = []
for _ in range(n):
    a, b = map(int, input().split())
    kimbop.append((a, b))

price = []
price.append(price1)

for i in range(n):
    price.append((1000 / kimbop[i][1]) * kimbop[i][0])

print(min(price))
