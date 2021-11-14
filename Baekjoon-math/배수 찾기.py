n = int(input())

while(True):
    num = int(input())
    if num == 0:
        break
    if num % n == 0:
         print("%s is a multiple of %s." % (num, n))
    else:
        print("%s is NOT a multiple of %s." % (num, n))
