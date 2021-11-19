import sys

n = int(sys.stdin.readline())
stack = []
for i in range(n):
    stack.append(int(input()))

max = stack[-1]
cnt = 1
for i in range(len(stack)-1, -1, -1):
    if stack[i] > max:
        cnt += 1
        max = stack[i]

print(cnt)
