def get_number_of_teams() -> int:
    '''
    function that gets the number of teams to play in the tournament
    number of teams must be at least 2 and an even amount
    '''
    MIN_NUM_TEAMS = 2
    while True:
        num_teams = int(input('Enter the number of teams in the tournament: '))
        if num_teams < MIN_NUM_TEAMS:
            print(f'The minimum number of teams is {MIN_NUM_TEAMS}, try again.')
        elif num_teams % MIN_NUM_TEAMS == 0 and num_teams >= MIN_NUM_TEAMS:
            break
    
    return num_teams

def get_team_names(num_teams) -> dict:
    '''
    function that gets the name of the team for each team
    '''
    team_names = {}
    for team in range(1,num_teams+1):
        team_num = f'team #{str(team)}'

        while True:
            name_of_team = input(f'Enter a name for {team_num}: ')
            if len(name_of_team) < 2:
                print("Team names must have at least 2 characters, try again.")
            elif len(name_of_team.split()) > 2:
                print("Team names may have at most 2 words, try again.")
            else: break
        team_names[team] = name_of_team
    
    return team_names

def get_number_of_games_played(num_teams) -> int:
    '''
    function that gets the number of games played by each team
    each team must play at least once
    '''
    while True:
        games_played = int(input("Enter the number of games played by each team: "))

        if games_played >= num_teams - 1:
            break
        
        print("Invalid number of games. Each team plays each other at least" + \
              " once in the regular season")

    return games_played

def get_team_wins(team_names, games_played):
    '''
    function that gets the numbe of wins for each team
    constraints: wins must be between 0 and number of games played 
    '''
    team_wins = []

    for team in team_names.values():
        while True:
            wins = int(input(f"Enter the number of wins Team {team} had: "))

            if wins >= 0 and wins <= games_played:
                break
            elif wins < 0:
                print("The minimum number of wins is 0, try again.")
            elif wins > games_played:
                print(f"The maximum number of wins is {games_played}, try again.")
        
        team_wins.append((team, wins))
    
    return team_wins

def sort_by_second_item(item):
    return item[1]

num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)

print("Generating the games to be played in the first round of the tournament...")
sorted_teams = sorted(team_wins, key=sort_by_second_item)
game_pairings = []

games_to_make = len(sorted_teams) // 2 #can only be the amount of -> teams
                                       #divided by 2 (one versus one per game)

for game_num in range(games_to_make):
    home_team = sorted_teams[game_num][0]
    away_team = sorted_teams[num_teams - 1 - game_num][0]
    game_pairings.append([home_team, away_team])

for pairing in game_pairings:
    home_team, away_team = pairing
    print(f"Home: {home_team} VS Away: {away_team}")