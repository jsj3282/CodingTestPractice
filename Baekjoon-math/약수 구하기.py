# Solution 1

arr = []
n, k = map(int, input().split())

for i in range(1, n + 1):
    if n % i == 0:
        arr.append(i)

if len(arr) < k:
    print(0)
else:
    print(arr[k - 1])
    
# Solution 2

import sys
# sys.stdin=open("input.txt", "rt")  # read text

# K번째 약수
n, k = map(int, input().split())
cnt = 0

for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:                   # for문이 break를 안거치고 정상적으로 종료되면 else 실행
    print(-1)
