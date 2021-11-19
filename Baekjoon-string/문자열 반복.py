T = int(input())

for i in range(T):
    r, s = input().split()
    p = ""
    for j in range(len(str(s))):
        p += s[j] * int(r)
    print(p)
