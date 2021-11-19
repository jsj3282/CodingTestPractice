while True:
    a, b, c, d = map(int, input().split())
    if a == b == c == d == c:
        break
    print(c - b, d - a)
