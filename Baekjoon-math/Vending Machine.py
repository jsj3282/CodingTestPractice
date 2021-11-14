button = list(map(int, input().split()))

drink = {
    1:500,
    2:800,
    3:1000
}
money = 5000
for i in button:
    money -= drink[i]

print(money)
