T = int(input())
for _ in range(T):
    n = int(input())
    number = list(map(int, input().split()))
    print(min(number), max(number))
