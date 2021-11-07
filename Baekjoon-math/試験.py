A, B, C = map(int, input().split())
test = [A, B, C]
test.sort(reverse=True)
 
print(test[0] + test[1])
