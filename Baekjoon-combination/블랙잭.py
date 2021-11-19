import itertools

n, m = map(int, input().split())
card = list(map(int, input().split()))

total = 0
diff = 2174000000

for com in itertools.combinations(card, 3):
    tmp1 = sum(com)
    tmp2 = m - tmp1
    if tmp2 < diff and tmp2 >= 0:
        diff = tmp2
        total = tmp1

print(total)
