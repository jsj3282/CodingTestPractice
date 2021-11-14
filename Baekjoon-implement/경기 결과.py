import sys

n = int(input())
a_w = 0
b_w = 0

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        a_w += 1
    elif b > a:
        b_w += 1

print(a_w, b_w)
