def comp(array1, array2):
    # your code
    print(array1, array2)
    if array1 == None or array2 == None:
        return False
    else:
        x = [i ** 2 for i in array1]
        return sorted(x) == sorted(array2)


    # '''
    # SOLUTION 2:
    # '''


def comp(array1, array2):
    # your code
	return False if array1 == None or array2 == None else sorted([i**2 for i in array1]) == sorted(array2)
