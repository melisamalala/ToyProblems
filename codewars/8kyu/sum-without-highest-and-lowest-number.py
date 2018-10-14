# Sum all the numbers of the array (in F# and Haskell you get a list)
# except the highest and the lowest element (the value, not the index!).
# (The highest/lowest element is respectively only one element
# at each edge, even if there are more than one with the same value!)

Video Link:
Codewars Link:

# Solution:

# BDD:
# first you sort the array from the lowest to the highest
# the lowest index will be at 0, the highest index will be the last index
# which will be found or positioned at -1


# PSEUDO CODE:
# arr = [5, 3, 18, 1, 30]
# sorted (arr) = [1, 3, 5, 18, 30]
# sorted (arr, key=int)
# Just a note: to sort from high low you write:
# sorted (arr, key=int, reverse = True)


def sum_array(arr):
    array =[]
    sorted(array)

