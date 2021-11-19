words = input().upper()

no_dupli_words = list(set(words))

cnt = []

for i in no_dupli_words:
    cnt.append(words.count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    max_index = cnt.index(max(cnt))
    print(no_dupli_words[max_index])
