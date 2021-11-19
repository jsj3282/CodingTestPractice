t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    a_area = a * a
    b_area = b * b
    print(a_area // b_area)
