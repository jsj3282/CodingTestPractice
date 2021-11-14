cute = 0
not_cute = 0

n = int(input())

for _ in range(n):
    survey = int(input())
    if survey == 1:
        cute += 1
    else:
        not_cute += 1

if cute > not_cute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
