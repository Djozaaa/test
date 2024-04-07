count_of_teams = 2
teams = []
for i in range(count_of_teams):
    print(i)
    team = {
        'id': i,
        'name': None,
        'score': 0
    }
    teams.append(team)

    team['name'] = input("Введіть назву команди:")
    team['score'] = int(input("Введіть суму забитих голів:"))


for u in (teams):
    print(u)


# test
   