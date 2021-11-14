T = int(input())
for _ in range(T):
    test = list(map(int, input().split()))
    test2 = []
    sum = 0
    for i in test:
        if i % 2 == 0:
            test2.append(i)
            sum += i
    test2.sort()
    #print(test2)
    print(sum, test2[0])
