def aggregate_pairs(arr):
    """
    Aggregate values for duplicate keys from a list of "key:value" strings,
    remove keys with a total value of 0, and return a dictionary sorted by keys.

    Args:
        arr (list of str): Input list containing strings in "key:value" format.

    Returns:
        dict: A dictionary where keys are strings, values are integers,
              duplicates are summed, keys with total value 0 are excluded,
              and keys are sorted alphabetically.
    """
    new_list = []
    empty_dic = {}
    for ele in arr:
        new_ele = ele.split(":")
        new_list.append(new_ele)
    for key, value in new_list:
        value = int(value)
        if key in empty_dic:
            empty_dic[key] += value
        else:
            empty_dic[key] = value

        if empty_dic[key] == 0:
            del empty_dic[key]

    sorted_keys = sorted(empty_dic)
    new_dict = {}
    for key in sorted_keys:
        new_dict[key] = empty_dic[key]

    return new_dict

    # return new_list


if __name__ == "__main__":
    my_list = ["A:2", "B:1", "X:3", "Y:0", "A:1", "X:0", "B:4"]
    my_func = aggregate_pairs(my_list)
    print(my_func)
