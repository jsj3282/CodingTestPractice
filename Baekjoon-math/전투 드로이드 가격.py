robot = [350.34, 230.90, 190.55, 125.30, 180.90]

T = int(input())

for _ in range(T):
    case = list(map(int, input().split()))
    sum = 0
    for i in range(len(case)):
        sum += case[i] * robot[i]
    print("${0}".format('%.2f' % sum))
