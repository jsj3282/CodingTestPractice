t, p = map(int, input().split())
 
if p > 20:
    a = t / (100 - p)
    answer = (p - 20) * a + (20 * 2 * a)
else:
    a = t / ((20 - p) * 2 + 80)
    answer = 2 * a * p
 
print(answer)
