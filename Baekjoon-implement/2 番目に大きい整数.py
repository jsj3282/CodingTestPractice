A, B, C = map(int, input().split())
 
N = [A, B, C]
 
N.sort(reverse=True)
 
print(N[1])
