t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    print(n // c + (1 if n % c else 0))
