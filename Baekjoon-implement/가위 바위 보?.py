t = int(input())

for _ in range(t):
    n = int(input())
    p1_cnt = p2_cnt = 0
    for _ in range(n):
        p1, p2 = input().split()
        if p1 == p2:
            continue
        elif (p1 == "R" and p2 == "S") or (p1 == "P" and p2 == "R") or (p1 == "S" and p2 =="P"):
            p1_cnt += 1
        else:
            p2_cnt += 1
    if p1_cnt > p2_cnt:
        print("Player 1")
    elif p2_cnt > p1_cnt:
        print("Player 2")
    else:
        print("TIE")
