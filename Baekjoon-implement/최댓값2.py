number = []
for _ in range(9):
    number.append(int(input()))

max_num = number[0]
max_index = 0

for i in range(len(number)):
    if number[i] > max_num:
        max_num = number[i]
        max_index = i

print(max_num)
print(max_index + 1)
