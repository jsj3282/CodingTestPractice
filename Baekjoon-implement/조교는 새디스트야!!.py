n = int(input())
student = list(map(int, input().split()))

n = 0
for i in range(len(student)):
    if student[i] != i + 1:
        n += 1

print(n)
