# Given the triangle of consecutive odd numbers:

             # 1
          # 3     5
       # 7     9    11
   # 13    15    17    19
# 21    23    25    27    29

# Calculate the row sums of this triangle from the row index
#  (starting at index 1) e.g.:


# SOLUTION:

def row_sum_odd_numbers(n):
    # sum of numbers in each row equals number of the row to the power of 3
    return n**3