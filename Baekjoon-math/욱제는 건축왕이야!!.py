n = int(input())

li = []
for _ in range(n):
    x, y = map(int, input().split())
    li.append((x, y))

round = 0
for i in range(1, n):
    round += (abs(li[i][0] - li[i-1][0]) ** 2 + abs(li[i][1] - li[i-1][1]) ** 2) ** 0.5

round += (abs(li[-1][0] - li[0][0]) ** 2 + abs(li[-1][1] - li[0][1]) ** 2) ** 0.5

print(int(round))
