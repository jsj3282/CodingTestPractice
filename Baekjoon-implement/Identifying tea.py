T = int(input())
a, b, c, d, e = map(int, input().split())
 
answer = [a, b, c, d, e]
 
count = 0
for i in answer:
    if i == T:
        count += 1
 
print(count)
