a, b = map(int, input().split())
 
i = 1
while(True):
    if b * i - a * i >= a:
        i += 1
        break
    i += 1
 
print(i)
