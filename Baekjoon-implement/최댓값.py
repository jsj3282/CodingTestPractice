arr = [[0 for j in range(9)] for i in range(9)]

for i in range(9):
    arr[i] = list(map(int, input().split()))

max_num = arr[0][0]
max_index = [0, 0]

for i in range(9):
    for j in range(9):
        if arr[i][j] > arr[max_index[0]][max_index[1]]:
            max_index[0] = i
            max_index[1] = j
            max_num = arr[i][j]

print(max_num)
print(max_index[0] + 1, max_index[1] + 1)
