T = int(input())

for _ in range(T):
    c, v = map(int, input().split())
    share = c // v
    res = c % v
    print("You get {0} piece(s) and your dad gets {1} piece(s).".format(share,res))
