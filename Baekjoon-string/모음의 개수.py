char = input()

vowel = ["a", "e", "i", "o", "u"]

res = 0

for i in vowel:
    res += char.count(i)

print(res)
