import itertools

li = []

for _ in range(9):
    li.append(int(input()))

for com in itertools.combinations(li, 7):
    if sum(com) == 100:
       for j in range(len(com)):
           print(com[j])
       break
