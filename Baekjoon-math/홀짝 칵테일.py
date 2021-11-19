cocktail = list(map(int, input().split()))

odd_cocktail = []

for i in range(3):
    if cocktail[i] % 2 != 0:
        odd_cocktail.append(cocktail[i])

res = 1
if len(odd_cocktail) == 0:
    for i in range(3):
        res *= cocktail[i]
else:
    for i in range(len(odd_cocktail)):
        res *= odd_cocktail[i]

print(res)
