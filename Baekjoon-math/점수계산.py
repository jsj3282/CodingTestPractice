n = int(input())

test = list(map(int, input().split()))

score = 0
point = 1
for i in test:
    if i == 0:
        point = 1
    else:
        score += i * point
        point += 1

print(score)
