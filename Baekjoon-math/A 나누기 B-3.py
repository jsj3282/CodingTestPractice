A, B = map(int, input().split())
 
C, D = divmod(A, B)
# print(C, D)
if A != 0 and B < 0:
    C, D = C + 1, D - B
 
print(C)
print(D)
