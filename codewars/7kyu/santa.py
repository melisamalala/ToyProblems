# https://www.codewars.com/kata/naughty-or-nice-1

# Victor's solution:
import calendar


def naughty_or_nice(data):
    ml = [len(data[calendar.month_name[x]]) for x in range(1, len(data))]
    mn = [calendar.month_name[x] for x in range(1, len(data))]
    print(ml, mn)
    year = []
    nice = []
    for x in range(0, 11):
        ls = data[mn[x]]
        count = len([ls[x] for x in ls if ls[x] == 'Nice'])
        days = len(ls)
        year.append(days)
        nice.append(count)

    print(sum(year), sum(nice))
    if sum(year) / sum(nice) > 0.5:
        return 'Nice!'
    else:
        return 'Naughty!'
