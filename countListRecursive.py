def count(num_list):
    """Counts items in a list using recursion"""

    if num_list:
        return 1 + count(num_list[:-1])
    else:
        return 0



print count([1, 5, 7])

print count([1, 5, 7, 9])

print count([1, 5, "ape"])