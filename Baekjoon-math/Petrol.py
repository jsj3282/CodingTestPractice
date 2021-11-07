n = int(input())
k = int(input())
 
if n <= k + 60:
    print(1500 * n)
else:
    a = ((k + 60) * 1500)
    b = ((n - (k + 60)) * 3000)
    print(a + b)
