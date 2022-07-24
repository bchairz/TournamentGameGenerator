# Write your code here.

def get_number_of_teams():
    MIN_NUM_TEAMS = 2
    while True:
        num_teams = int(input('Enter the number of teams in the tournament: '))
        if num_teams < MIN_NUM_TEAMS:
            print(f'The minimum number of teams is {MIN_NUM_TEAMS}, try again.')
        elif num_teams % MIN_NUM_TEAMS == 0 and num_teams >= MIN_NUM_TEAMS:
            break
    
    return num_teams

def get_team_names(num_teams):
    pass


def get_number_of_games_played(num_teams):
    pass


def get_team_wins(team_names, games_played):
    pass


# It is not necessary to use the functions defined above. There are simply here
# to help give your code some structure and provide a starting point.
num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)

print("Generating the games to be played in the first round of the tournament...")
