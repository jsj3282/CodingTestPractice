N = int(input())
answer = 0
for n in range(1, N + 1):
    for i in range(n + 1):
        answer += n + i
 
print(answer)
