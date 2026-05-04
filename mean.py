team = {
    "Virat": 180,
    "Rohit": 175,
    "Gill": 178
}

captain = [name for name in team if team[name] == max(team.values())][0]

print("Captain (tallest):", captain)