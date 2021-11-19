n, T = map(int, input().split())

job = list(map(int, input().split()))

result = 0

for i in job:
    T -= i
    if T < 0:
        break
    result += 1

print(result)
