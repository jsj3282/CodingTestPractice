day = int(input())
car = list(map(int, input().split()))
 
i = 0
for c in car:
    if c == day:
        i += 1
 
print(i)
