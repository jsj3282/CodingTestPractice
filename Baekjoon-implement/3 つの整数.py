A, B, C = map(int, input().split())
ABC = [A, B, C]
count1 = 0
count2 = 0
 
for i in ABC:
    if i == 1:
        count1 += 1
    else:
        count2 += 1
 
if count1 > count2:
    print(1)
else:
    print(2)
