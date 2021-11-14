sample_case, system_case = map(int, input().split())

sum1 = 0
for _ in range(sample_case):
    a, b = map(int, input().split())
    if a == b:
        sum1 += 1

sum2 = 0
for _ in range(system_case):
    a, b = map(int, input().split())
    if a == b:
        sum2 += 1

if sum1 == sample_case and sum2 == system_case:
    print("Accepted")
elif sum1 != sample_case:
    print("Wrong Answer")
else:
    print("Why Wrong!!!")
