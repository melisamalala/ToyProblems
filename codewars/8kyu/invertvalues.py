# Invert values

# Description:
#Given a set of numbers,
#  return the additive inverse of each.
# Each positive becomes negatives,
# and the negatives become positives.

# Video to my solution: https://youtu.be/oLg7Ojk1muM


# SOLUTION:

def invert(lst):
    list = []
    for item in lst:
        item = item * -1
        list.append(item)
    return list

print(invert([1, 2, 3, -4, -5]))


# COMPREHENSIVE SOLUTION:

def invert(lst):
    return [-x for x in lst]