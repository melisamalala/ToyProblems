# Victors Solution

# how_much_coffee()


def how_much_coffee(e):
    count = 0
    etm = ['cw', 'dog', 'cat', 'movie']
    if e == []:
        return count
    else:
        for ev in e:
            if ev.islower() and ev in etm:
                count += 1
            elif ev.isupper() and ev.lower() in etm:
                count += 2

    if count > 3:
        return 'You need extra sleep'
    return count



# List Comprehension by Victor Ireri:

def how_much_coffee(e):
    etm = ['cw', 'dog', 'cat', 'movie', 'CW', 'DOG', 'CAT', 'MOVIE']
    count = sum([1 if i.islower() else 2 for i in e if i in etm])
    return [0 if count == 0 else count if count < 4 else 'You need extra sleep'][0]


