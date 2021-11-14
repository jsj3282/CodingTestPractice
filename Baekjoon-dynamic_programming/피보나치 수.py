# Solution 1

n = int(input())

a, b = 0, 1
for i in range(n):
    a, b = b, a + b
print(a)

# Solution 2

n = int(input())
A = [0 for i in range(n+2)]
A[1] = 1

for n in range(2, n+2):
    A[n] = A[n-1] + A[n-2]
print(A[n-1])
