# Solution 1

n = int(input())
if n <= 0:
    print("divide by zero")
else:
    record = list(map(int, input().split()))
    mean_record = sum(record) / n
    expect_record = 0
    for i in range(n):
        expect_record += record[i] / n
    answer = mean_record / expect_record
    print("%.2f" %answer)
    
# Solution 2

N = int(input())
if N == 0:
    print("divide by zero")
else:
    print(1.00)
