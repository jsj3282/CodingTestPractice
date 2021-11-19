n = int(input())
market = list(map(int, input().split()))

cnt = 0
current_milk = 0

for i in range(len(market)):
    if market[i] == (current_milk) % 3:
        cnt += 1
        current_milk += 1
    
print(cnt)
