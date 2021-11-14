while(True):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    share = a // b
    res = a % b
    print(share, res, "/", b)
