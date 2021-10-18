apple = int(input())
more = int(input())
 
if apple % 2 == 0:
    claudia = apple // 2 + more // 2
    natalia = apple // 2 - more // 2
else:
    claudia = apple // 2 + more // 2 + 1
    natalia = apple // 2 - more // 2
 
print(claudia)
