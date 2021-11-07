mirko = float(input())
 
# 연비 : 1.609344 / 3.785411784 (1리터 당 갈수있는 킬로미터)
 
answer = 100.0 / (mirko * (1.609344 / 3.785411784))
 
print("%.6f" % answer)
