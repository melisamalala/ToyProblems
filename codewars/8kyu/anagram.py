def anagram (s1, s2):


    # Remove spaces and lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s1.replace(" ", "").lower()

    return sorted (s1) == sorted(s2)