import math
n = int(input())
 
price = [float(input()) for _ in range(3)]
# print(price)
for i in price:
    print("$%.02f" % round(i * 0.8, 2))
