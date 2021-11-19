a, b = map(int, input().split())
c, d = map(int, input().split())

rot0 = a / c + b / d
rot1 = c / d + a / b
rot2 = d / b + c / a
rot3 = b / a + d / c

rot = [rot0, rot1, rot2, rot3]
rot_max = max(rot)
print(rot.index(rot_max))
