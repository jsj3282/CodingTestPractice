X, L, R = map(int, input().split())
abs_list = []
 
for i in range(L, R + 1):
    abs_list.append((i, abs(X - i)))
 
abs_list.sort(key = lambda value: (value[1], value[0]))
 
print(abs_list[0][0])
