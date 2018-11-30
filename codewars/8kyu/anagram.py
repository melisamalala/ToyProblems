def anagram (s1, s2):


    # Remove spaces and lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s1.replace(" ", "").lower()

    # Check if the sorted s1 and s2 are similar
    return sorted (s1) == sorted(s2)


def anagram (s1, s2):


    # Remove spaces and lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s1.replace(" ", "").lower()

    # Check if same number of letters
    if len(s1) != len(s2):
        return False

    # count frequency of each letter
    count = {}

    for i in s1:
        # for every letter in first string
        if i in count:
            count [i] +=1

        else:
            count [i] = 1

    for i in s2:
        if i in count:
            count[i] -= 1

        else:
            count[i] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True


