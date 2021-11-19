li = list(map(int, input().split()))

li.sort()

if li[1] - li[0] == li[2] - li[1]:
    print(li[2] * 2 - li[1])
elif li[2] - li[1] > li[1] - li[0]:
    print(li[1] * 2 - li[0])
else:
    print(li[1] * 2 - li[2])
