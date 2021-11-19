a = list(input().split())
b = ""
for i in range(len(a)):
    b += str(a[i])

if b == "12345678":
    print("ascending")
elif b == "87654321":
    print("descending")
else:
    print("mixed")
