n = int(input())

li = [i ** 2 for i in range(1, 501)]

cnt = 0

for i in range(1, 500):
    for j in range(0, i):
        if li[i] - li[j] == n:
            cnt += 1

print(cnt)
