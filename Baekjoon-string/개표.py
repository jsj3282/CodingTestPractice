v = int(input())

s = input()

a_c, b_c = 0, 0

for i in range(v):
    if s[i] == "A":
        a_c += 1
    else:
        b_c += 1

if a_c > b_c:
    print("A")
elif b_c > a_c:
    print("B")
else:
    print("Tie")
