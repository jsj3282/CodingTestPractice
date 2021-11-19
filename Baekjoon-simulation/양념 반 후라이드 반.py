a, b, c, x, y = map(int, input().split())

if a + b < 2 * c:
    print(a * x + b * y)
else:
    res = min(x, y) * 2 * c
    if x >= y:
        dif = x - y
        res += min(a * dif, 2 * c * dif)
    else:
        dif = y - x
        res += min(b * dif, 2 * c * dif)
    print(res)
