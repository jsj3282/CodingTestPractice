a3 = int(input())
a2 = int(input())
a1 = int(input())
b3 = int(input())
b2 = int(input())
b1 = int(input())
 
if a3 * 3 + a2 * 2 + a1 > b3 * 3 + b2 * 2 + b1:
    print("A")
elif b3 * 3 + b2 * 2 + b1 > a3 * 3 + a2 * 2 + a1:
    print("B")
else:
    print("T")
