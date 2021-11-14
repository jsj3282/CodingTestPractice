T = int(input())

for _ in range(T):
    y_w, k_w = 0, 0
    for i in range(9):
        y, k = map(int, input().split())
        if y > k:
            y_w += 1
        elif y < k:
            k_w += 1
    if y_w > k_w:
        print("Yonsei")
    elif y_w < k_w:
        print("Korea")
    else:
        print("Draw")
