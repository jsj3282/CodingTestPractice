n = int(input())
if n <= 5:
    print(n)
else:
    a = (n - 5) // 4
    b = (n - 5) % 4
    if a % 2 == 1:
        print(1 + b)
    else:
        print(5 - b)
