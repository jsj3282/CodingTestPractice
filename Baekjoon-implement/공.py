cup = [0, 1, 2, 3]
 
M = int(input())
 
for _ in range(M):
    cup1, cup2 = map(int, input().split())
    cup[cup1], cup[cup2] = cup[cup2], cup[cup1]
 
# print(cup)
print(cup.index(1))
