for _ in range(int(input())):
    c = int(input())
    d = [25, 10, 5, 1]
    li = []
    for n in d:
        li.append(c // n)
        c = c % n
    print(*li)
