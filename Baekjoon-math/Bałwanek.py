park, first = map(int, input().split())
 
#park *= 1000
#first *= 1000
 
if first * 7 <= park:
    print(first * 7000)
elif first * 3.5 <= park:
    print(first * 3500)
elif first * 1.75 <= park:
    print(first * 1750)
else:
    print(0)
