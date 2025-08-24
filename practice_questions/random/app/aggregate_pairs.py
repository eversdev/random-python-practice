def aggregate_pairs(arr):
    new_list = []
    for ele in arr:
        new_ele = ele.split(":")
        new_list.append(new_ele)
    return new_list


my_list = ["A:2", "B:1", "X:3", "Y:0", "A:1", "X:0", "B:4"]


my_func = aggregate_pairs(my_list)
print(my_func)
