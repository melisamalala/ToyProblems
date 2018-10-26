def getTotal(costs, items, tax):
    total = 0
    for i in items:
        if i in costs:
            total += costs[i]
    return round(total * (1 + tax), 2)