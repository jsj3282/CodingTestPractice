max_index = 0
max_score = 0
for i in range(5):
    score = list(map(int, input().split()))
    if max_score < sum(score):
        max_score = sum(score)
        max_index = i

print(max_index + 1, max_score)
