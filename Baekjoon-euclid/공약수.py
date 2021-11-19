import sys

# 최대 공약수 구하는 함수
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
# n은 2 또는 3
g = gcd(li[0], gcd(li[1], li[-1]))

# 최대공약수의 약수 출력(최대공약수의 절반까지만 검사)
for i in range(1, (g // 2) + 1):
    if g % i == 0:
        print(i)
# 마지막에는 자기 자신을 출력
print(g)
