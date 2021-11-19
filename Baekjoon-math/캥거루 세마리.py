a, b, c = map(int, input().split())

k = [a, b, c]

cnt = 0

while True:
    if k[1] - k[0] > k[2] - k[1]:
        k[2] = k[1] - 1
        k.sort()
        cnt += 1
    else:
        k[0] = k[1] + 1
        k.sort()
        cnt += 1

    if k[0] == k[1] or k[1] == k[2]:
        break

print(cnt - 1)
