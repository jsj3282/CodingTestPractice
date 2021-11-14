while(True):
    side1, side2, side3 = map(int, input().split())
    side = [side1, side2, side3]
    side.sort()
    if side1 == 0 and side2 == 0 and side3 == 0:
        break
    if side[2] >= side[0] + side[1]:
        print("Invalid")
    else:
        if side1 == side2 == side3:
            print("Equilateral")
        elif side1 != side2 and side1 != side3 and side2 != side3:
            print("Scalene")
        else:
            print("Isosceles")
