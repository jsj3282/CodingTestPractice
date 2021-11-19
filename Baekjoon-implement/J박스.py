T = int(input())

jbox = []

for _ in range(T):
    jbox.append(int(input()))

for i in jbox:
    if i < 3:
        for j in range(i):
            print("#" * i)
        print()
    else:
        print("#" * i)
        for j in range(i - 2):
            print("#"+"J" * (i - 2) +"#")
        print("#" * i)
        print()
