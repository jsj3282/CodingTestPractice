A = int(input())
B = int(input())
C = int(input())

num = list(str(A * B * C))

for i in range(10):
    num_count = num.count(str(i))
    print(num_count)
