start = input()
end = input()
 
start_list = start.split(":")
end_list = end.split(":")
 
start_list = list(map(int, start_list))
end_list = list(map(int, end_list))
 
start_second = start_list[0] * 60 * 60 + start_list[1] * 60 + start_list[2]
end_second = end_list[0] * 60 * 60 + end_list[1] * 60 + end_list[2]
 
if start_second > end_second:
    end_second += 24 * 60 * 60
 
print(end_second - start_second)
