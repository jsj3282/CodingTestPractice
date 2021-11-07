import math
 
kozik, coach, strike = map(int, input().split())
 
height = coach - kozik
 
 
print(math.ceil(height/strike))
