value1 = int(input())
value2 = int(input())
value3 = int(input())
value4 = int(input())
 
 
if value1 < value2 and value2 < value3 and value3 < value4:
    print("Fish Rising")
elif value1 > value2 and value2 > value3 and value3 > value4:
    print("Fish Diving")
elif value1 == value2 and value2 == value3 and value3 == value4:
    print("Fish At Constant Depth")
else:
    print("No Fish")
