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
    team_names = {}
    for team in range(1,num_teams+1):
        team_num = f'team #{str(team)}'
        print(team_num) #debug statement for verifying which team we are looking at
        while True:
            name_of_team = input(f'Enter a name for {team_num}: ')
            if len(name_of_team) < 2:
                print("Team names must have at least 2 characters, try again.")
            if len(name_of_team.split()) > 2:
                print("Team names may have at most 2 words, try again.")
            else: break
        team_names[team] = name_of_team
    # for item in team_names.items():
        # print(item)
    return team_names
def get_number_of_games_played(num_teams) -> int:
    while True:
        games_played = int(input("Enter the number of games played by each team: "))

        if games_played >= num_teams - 1:
            break
        
        print("Invalid number of games. Each team plays each other at least" + \
              "once in the regular season")

    return games_played



def get_team_wins(team_names, games_played):
    pass


# It is not necessary to use the functions defined above. There are simply here
# to help give your code some structure and provide a starting point.
num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)

print("Generating the games to be played in the first round of the tournament...")
