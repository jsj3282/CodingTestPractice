stick1, stick2, stick3 = map(int, input().split())
 
stick = [stick1, stick2, stick3]
 
stick.sort()
 
if stick[0] ** 2 + stick[1] ** 2 == stick[2] ** 2:
    print(1) 
elif stick[0] == stick[1] == stick[2]:
    print(2)
else:
    print(0)
