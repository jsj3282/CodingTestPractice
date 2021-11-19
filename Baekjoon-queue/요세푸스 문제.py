from collections import deque

n, k = map(int, input().split())

q = [i for i in range(1, n+1)]
q = deque(q)

res = []

while q:
    for _ in range(k-1):
        cur = q.popleft()
        q.append(cur)
    res.append(str(q.popleft()))

print("<", ", ".join(res)[:], ">", sep = '')
