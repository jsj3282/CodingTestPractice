book = []
total = int(input())
for _ in range(9):
    book.append(int(input()))

print(total - sum(book))
