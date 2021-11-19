n = int(input())

a = [i for i in range(1, n + 1)]

while len(a) > 1:
    print(a.pop(0), end=" ")
    a.append(a.pop(0))
    # print(a)
print(a[0])
