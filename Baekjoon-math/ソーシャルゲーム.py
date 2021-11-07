A, B, C = map(int, input().split())
 
i = 1
while(True):
    C -= A
    if i % 7 == 0:
        C -= B
    if C <= 0:
        break
    i += 1
 
print(i)
