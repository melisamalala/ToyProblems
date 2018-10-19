# Codewar Link:


# VICTOR IRERI'S SOLUTION:
import re


def mix(s1, s2):
    cs1 = ''.join(re.findall('[a-z]', s1))
    cs2 = ''.join(re.findall('[a-z]', s2))
    ls1 = []
    ls2 = []

    while cs1 != '':
        ls1.append(''.join(re.findall(cs1[0], cs1)))
        cs1 = re.sub(cs1[0], '', cs1)

    while cs2 != '':
        ls2.append(''.join(re.findall(cs2[0], cs2)))
        cs2 = re.sub(cs2[0], '', cs2)

    ls1 = [i for i in ls1 if len(i) > 1]
    ls2 = [i for i in ls2 if len(i) > 1]
    fls1 = [f'1:{i}' if i not in ls2 else f'=:{i}' for i in ls1]
    fls2 = [f'2:{i}' if i not in ls1 else f'=:{i}' for i in ls2]
    x = list(set(fls1 + fls2))

    for e, i in enumerate(x):
        for e1, y in enumerate(x):
            if i[-1] in y and len(y) > len(i):
                x.remove(i)
            elif i[-1] in y and len(y) < len(i):
                x.remove(y)

    x.sort()
    x.sort(key=len, reverse=True)
    fn = '/'.join(x)
    return fn