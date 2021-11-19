t = int(input())

for _ in range(t):
    n = int(input())
    print("Pairs for %d:" %n, end = " ")

    start = 1

    for i in range((n - 1) // 2):
        if i != 0:
            print(",", end = " ")           # ,를 앞에다가 찍음 
        print(start, n - start, end= "")    
        start += 1

    print()
