A, B = map(int, input().split())

m = max(A, B)
n = min(A, B)
sum = (A + B) * (m - n + 1) / 2
print(int(sum))
