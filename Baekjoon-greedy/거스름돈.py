money = [500, 100, 50, 10, 5, 1]

t = 1000 - int(input())

res = 0

for i in money:
    res += t // i
    t = t % i
    # print(res, t)
    if t == 0:
        break

print(res)
