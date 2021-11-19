import sys

n = int(input())

for i in range(1, n+1):
    a = sys.stdin.readline().rstrip().split()
    b = ' '.join(a[::-1])
    print(f"Case #{i}: {b}")
