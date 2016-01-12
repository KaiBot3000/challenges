# # O(n^2)
# def missingNum(num_list, max):
#     """Given a list of numbers missing one number, and the maximum num in the list, return missing num"""

#     for num in range(1, (max + 1)):
#         if num not in num_list:
#             return num

#     return 0


# # O(n)
# def missingNum(num_list, max):
#     """Given a list of numbers missing one number, and the maximum num in the list, return missing num"""
    
#     num_set = set(num_list)
#     for num in range(1, (max + 1)):
#         if num not in num_set: # sets are O(1) for 'in'
#             return num

#     return 0


# # O(n log n)
# def missingNum(num_list, max):
#     """Given a list of numbers missing one number, and the maximum num in the list, return missing num"""
    
#     num_list.sort()
#     i = 1

#     for num in num_list:
#         if num is not i:
#             return i
#         else:
#             i += 1

#     return 0

# O(n)
def missingNum(num_list, max):
    """Given a list of numbers missing one number, and the maximum num in the list, return missing num"""
    
    expected = sum(range(max + 1))
    total = sum(num_list)

    return expected - total


print missingNum([1, 2, 4], 4) # -> 3

print missingNum([1, 2, 6, 5, 3], 6) # -> 4