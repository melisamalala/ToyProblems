def comp(array1, array2):
    # your code
    print(array1, array2)
    if array1 == None or array2 == None:
        return False
    else:
        x = [i ** 2 for i in array1]
        return sorted(x) == sorted(array2)

