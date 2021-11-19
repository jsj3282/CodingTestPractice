a = []

for i in range(10):
    a.append(int(input()))

print(sum(a) // 10)             # 평균
print(max(a, key=a.count))      # 최빈값
