"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list
    """

    # add nums to set
    num_set = set(nums)
    
    # iterate through max
    for number in range(max_num):
        if number not in num_set:
            return number


print missing_number([0, 1, 2, 4], 5)

# Doctests weren't included in this stub :/
# if __name__ == '__main__':
#     import doctest
#     if doctest.testmod().failed == 0:
#         print "\n*** ALL TESTS PASS. NICELY DONE!\n"
