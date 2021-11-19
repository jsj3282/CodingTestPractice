while True:
    n = int(input())
    if n == 0:
        break
    while True:
        n = sum(list(map(int, str(n))))
        #print(n)
        if n // 10 == 0:
            print(n)
            break
