The only known Wilson prime numbers are 5, 12 and 563.
If there are any other wilson promes, they must be greater than 2 x 10^13.


import math
def am_i_wilson(n):
    if n == 5 or n == 13 or n == 563:
        return True
    else:
        return False