Ca, Ba, Pa = map(int, input().split())
Cr, Br, Pr = map(int, input().split())
 
C = Cr - Ca if Cr > Ca else 0
B = Br - Ba if Br > Ba else 0
P = Pr - Pa if Pr > Pa else 0
 
print(C + B + P)
