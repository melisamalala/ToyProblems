def duck_duck_goose(players, goose):
    i = goose % (len(players))
    return players[i - 1].name
    # ...