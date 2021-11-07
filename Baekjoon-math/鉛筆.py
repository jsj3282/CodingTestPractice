N, A, B, C, D = map(int, input().split())
 
X = (N // A + (1 if N % A != 0 else 0)) * B
#print(X)
Y = (N // C + (1 if N % C != 0 else 0)) * D
#print(Y)
 
print(min(X, Y))
