start = input()
q = 0
while True:
    w = input()
    if w == "문제":
        q += 1
    elif w == "고무오리":
        if q != 0:
            q -= 1
        else:
            q += 2
    elif w == "고무오리 디버깅 끝":
        if q <= 0:
            print("고무오리야 사랑해")
            break
        else:
            print("힝구")
            break
