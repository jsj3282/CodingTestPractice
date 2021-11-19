a, b = input().split()
s_a = int(a[::-1])      # [::-1] : 역순
s_b = int(b[::-1])

print(s_a) if s_a > s_b else print(s_b)
