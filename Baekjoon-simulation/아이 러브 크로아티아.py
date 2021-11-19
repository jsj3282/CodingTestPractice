k = int(input()) - 1
n = int(input())
li = [input().split() for _ in range(n)]

time = 0

for i, j in li:
    time += int(i)
    if time >= 210:
        print(k + 1)
        break
    if j == 'T':
        k = (k + 1) % 8
