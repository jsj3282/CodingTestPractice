A, B, C, D = map(int, input().split())

turtle = [A, B, C, D]

turtle.sort(reverse=True)

print(turtle[1] * turtle[-1])
