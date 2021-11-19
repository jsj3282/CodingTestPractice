import sys

while True:
    line = sys.stdin.readline().rstrip("\n")

    if not line:
        break

    # 소문자, 대문자, 숫자, 공백
    l, u, d, s = 0, 0, 0, 0
    for i in line:
        if i.islower():
            l += 1
        elif i.isupper():
            u += 1
        elif i.isdigit():
            d += 1
        elif i.isspace():
            s += 1
    
    print(l, u, d, s)
