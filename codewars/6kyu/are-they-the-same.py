def comp(array1, array2):
    # your code
    x = [i ** 2 for i in array1]
    return (set(x) == set(array2))

