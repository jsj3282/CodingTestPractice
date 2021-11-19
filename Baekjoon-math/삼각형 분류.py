t = int(input())
for i in range(t):
    li = list(map(int, input().split()))
    li.sort()
    if li[0] + li[1] <= li[2]:
        print(f"Case #{i + 1}: invalid!")
    else:
        if li[0] == li[1] == li[2]:
            print(f"Case #{i + 1}: equilateral")
        elif li[0] == li[1] or li[1] == li[2] or li[0] == li[2]:
            print(f"Case #{i + 1}: isosceles")
        elif li[0] != li[1] != li[2]:
            print(f"Case #{i + 1}: scalene")
