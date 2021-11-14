import sys

Q = int(input())

for _ in range(Q):
    num = int(sys.stdin.readline())
    if (num & (-num)) == num:
        print(1)
    else:
        print(0)
