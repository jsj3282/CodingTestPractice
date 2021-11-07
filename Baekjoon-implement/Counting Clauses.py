n, m = map(int, input().split())
 
sat = []
for _ in range(n):
    sat2 = list(map(int, input().split()))
    sat.append(sat2)
 
if n < 8:
    print("unsatisfactory")
else:
    print("satisfactory")
