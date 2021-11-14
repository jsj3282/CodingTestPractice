temp = []
while(True):
    num = float(input())
    if num == 999:
        break
    temp.append(num)
    if len(temp) == 1:
        continue
    else:
        result = temp[-1] - temp[-2]
        print("%.2f" % result)
