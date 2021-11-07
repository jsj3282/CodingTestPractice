import math
 
s_b = int(input())
j_b = int(input())
h_b = int(input())
cola = int(input())
cida = int(input())
 
burger = [s_b, j_b, h_b]
drink = [cola, cida]
 
set_menu = []
for i in burger:
    for j in drink:
        set_menu.append(i + j - 50)
 
print(min(set_menu))
