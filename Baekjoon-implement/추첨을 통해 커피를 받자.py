max_score = [100, 100, 200, 200, 300, 300, 400, 400, 500]

score = list(map(int, input().split()))

hacker = False
sum = 0

for i in range(len(score)):
    if score[i] > max_score[i]:
        hacker = True
        break
    else:
        sum += score[i]

if hacker:
    print("hacker")
else:
    if sum >= 100:
        print("draw")
    else:
        print("none")
