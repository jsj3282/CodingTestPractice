from itertools import combinations
 
player = int(input())
player_list = [i for i in range(1, 100)]
#print(player_list)
if player < 4:
    print(0)
else:
    p = list(combinations(player_list[:player-1], 3))
    #print(p)
    print(len(p))
