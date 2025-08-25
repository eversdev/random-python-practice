def aggregate_pairs(arr):
    """
    Split a list of "key:value" strings into lists of [key, value].

    Args:
        arr (list of str): Input list containing strings in "key:value" format.

    Returns:
        list: A list of [key, value] pairs, where key is a string and value is a string.
    """
    new_list = []
    for ele in arr:
        new_ele = ele.split(":")
        new_list.append(new_ele)
    return new_list


my_list = ["A:2", "B:1", "X:3", "Y:0", "A:1", "X:0", "B:4"]


my_func = aggregate_pairs(my_list)
print(my_func)
