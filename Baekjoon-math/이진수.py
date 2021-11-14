# Solution 1

T = int(input())

for _ in range(T):
    n = bin(int(input()))[2:]
    for i in range(len(n)):
        if n[-i-1] == '1':
            print(i, end = " ")
 
# Solution 2

for _ in range(int(input())):
    n = int(input())
    i = 0
    while n > 0:
        if n%2 == 1:
            print(i, end=' ')
        n = n//2
        i += 1
