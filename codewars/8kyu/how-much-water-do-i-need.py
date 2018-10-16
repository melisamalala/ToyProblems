# VICTORS SOLUTION:

import math

# VICTORS COMPREHENDED SOLUTION:
def how_much_water(W, L, C):
    return  ['Too much clothes' if C > 2 * L else 'Not enough clothes' if C < L else round((math.pow(1.1, C - L) * W), 2)][0]


   # WELL- EXPLAINED CODE

    if C > 2 * L:
        return 'Too much clothes'
    elif C < L:
        return 'Not enough clothes'
    else:
        r = C - L
        return round((math.pow(1.1, r) * W), 2)
    # Good luck!
    # Consider rate of progression