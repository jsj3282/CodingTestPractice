x, y, z = map(int, input().split())
if x + y == z:
    print(f"{x}+{y}={z}")
elif x - y == z:
    print(f"{x}-{y}={z}")
elif x * y == z:
    print(f"{x}*{y}={z}")
elif x // y == z:
    print(f"{x}/{y}={z}")
elif x == y + z:
    print(f"{x}={y}+{z}")
elif x == y - z:
    print(f"{x}={y}-{z}")
elif x == y * z:
    print(f"{x}={y}*{z}")
elif x == y // z:
    print(f"{x}={y}/{z}")
