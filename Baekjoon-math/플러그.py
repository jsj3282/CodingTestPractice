import sys

num = int(sys.stdin.readline())
sum = 1
for i in range(num):
    plug = int(sys.stdin.readline())
    sum+=plug

print(sum-num)
