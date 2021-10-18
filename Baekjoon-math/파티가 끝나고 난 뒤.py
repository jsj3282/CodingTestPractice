num, area = map(int, input().split())
article = list(map(int, input().split()))
 
total = num * area
 
for i in article:
    print(i - total, end=" ")
