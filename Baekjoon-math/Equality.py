import re
 
math_expression = input()
numbers = re.findall("\d+", math_expression)
numbers = list(map(int, numbers))
if numbers[0] + numbers[1] == numbers[2]:
    print("YES")
else:
    print("NO")
