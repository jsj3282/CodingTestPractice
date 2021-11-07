hour, minute = map(int, input().split())
cook = int(input())
 
if minute + cook >= 60:
    minute2 = (minute + cook) % 60
    hour += (minute + cook) // 60
    # print(hour)
    if hour > 23:
        hour -= 24
else:
    minute2 = minute + cook
 
print(hour, minute2)
