import math
 
minguk = list(map(int, input().split()))
manse = list(map(int, input().split()))
 
sum_minguk = sum(minguk)
sum_manse = sum(manse)
 
print(max(sum_minguk, sum_manse))
