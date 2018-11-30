'''
Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in an array like so: [index1, index2].

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two
different items from that array).

Example:
    nums = [1, 3, 11, 2, 7]
    target = 9
#     return : [3, 4]

9 - 1 = 8 -> {8: 0}
9 - 3 = 6 -> {8:0, 6:1}
9 - 11 = -2 -> {8:0, 6:1, -2:2 }
9 - 2 = 7 -> {8:0, 6:1, -2:2 , 7:3}


nums [i], i
'''

nums = [1, 3, 11, 2, 7]
target = 9

def two_sum(nums, target):
    if len(nums) <= 1:
        return False
    aux_dict={}

    for i in range(len(nums)):
        if nums[i] in aux_dict:
            return [aux_dict, nums[i]], i
        else:
            aux_dict[target - nums[i]] = i

print(two_sum(nums, target))
