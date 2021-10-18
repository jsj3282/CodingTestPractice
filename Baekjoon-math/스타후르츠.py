summer, fruitday, square, price = map(int, input().split())
 
day = (summer - 1) // fruitday
print(day * square * price)
