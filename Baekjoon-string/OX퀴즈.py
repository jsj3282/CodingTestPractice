T = int(input())

for i in range(T):
    score = 0
    test = str(input())
    temp = 1
    for i in range(len(test)):
        if test[i] == "O":
            score += temp
            temp += 1
        else:
            temp = 1
    print(score) 
