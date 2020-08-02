import pandas as pd

data = pd.read_csv('no_bad_names.csv')

# data['Fantasy_Points'] = data['PTS']+                                                                                                                        data['FG3M']*.5+                             data['REB']*1.25                                     +data['AST']*1.5+data['STL']*2+data['BLK']*2-data['TOV']*.5

data['Fantasy_Points'] = (data['made_free_throws']+(data['made_field_goals']-data['made_three_point_field_goals'])*2+data['made_three_point_field_goals']*3)+ data['made_three_point_field_goals']*.5 + (data['offensive_rebounds']+data['defensive_rebounds'])*1.25+data['assists']*1.5+data['steals']*2+data['blocks']*2-data['turnovers']*.5


data['PTS'] = (data['made_free_throws']+(data['made_field_goals']-data['made_three_point_field_goals'])*2+data['made_three_point_field_goals']*3)
data['REB'] = (data['offensive_rebounds']+data['defensive_rebounds'])

data['TD/DD1'] = data['PTS'].apply(lambda x: 1 if x >= 10 else 0)
data['TD/DD2'] = data['REB'].apply(lambda x: 1 if x >= 10 else 0)
data['TD/DD3'] = data['assists'].apply(lambda x: 1 if x >= 10 else 0)
data['TD/DD4'] = data['blocks'].apply(lambda x: 1 if x >= 10 else 0)
data['TD/DD5'] = data['steals'].apply(lambda x: 1 if x >= 10 else 0)

data['TD/DD'] = data['TD/DD1']+data['TD/DD2']+data['TD/DD3']+data['TD/DD4']+data['TD/DD5']

data['DD'] = data['TD/DD'].apply(lambda x: 1 if x == 2 else 0)
data['TD'] = data['TD/DD'].apply(lambda x: 1 if x > 2 else 0)

data['Fantasy_Points'] = data['Fantasy_Points'] + 1.5*data['DD'] + 3*data['TD']


data = data.drop(['TD/DD', 'TD/DD1', 'TD/DD2', 'TD/DD3', 'TD/DD4', 'TD/DD5', 'PTS', 'REB', 'DD', 'TD'], axis=1)



data = data.drop(['assists', 'attempted_field_goals', 'attempted_free_throws', 'attempted_three_point_field_goals', 
'blocks', 'defensive_rebounds', 'game_score', 'made_field_goals', 'made_free_throws',
'made_three_point_field_goals', 'offensive_rebounds', 'outcome', 'personal_fouls', 'seconds_played',
'slug', 'steals', 'turnovers'], axis=1)

data['location'] = data['location'].replace('Location.', '', regex=True)
data['opponent'] = data['opponent'].replace('Team.', '', regex=True)
data['team'] = data['team'].replace('Team.', '', regex=True)

abb = ['ATL', 'BOS', 'BKN', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET',
'GS', 'HOU', 'IND', 'LAC','LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NO', 'NY', 
'OKC', 'ORL', 'PHI', 'PHX', 'POR', 'SAC', 'SA', 'TOR', 'UTA', 'WAS']

full = ['ATLANTA_HAWKS', 'BOSTON_CELTICS', 'BROOKLYN_NETS', 'CHARLOTTE_HORNETS', 'CHICAGO_BULLS', 
'CLEVELAND_CAVALIERS', 'DALLAS_MAVERICKS', 'DENVER_NUGGETS', 'DETROIT_PISTONS', 'GOLDEN_STATE_WARRIORS',
'HOUSTON_ROCKETS', 'INDIANA_PACERS', 'LOS_ANGELES_CLIPPERS', 'LOS_ANGELES_LAKERS', 'MEMPHIS_GRIZZLIES',
'MIAMI_HEAT', 'MILWAUKEE_BUCKS', 'MINNESOTA_TIMBERWOLVES', 'NEW_ORLEANS_PELICANS', 'NEW_YORK_KNICKS', 
'OKLAHOMA_CITY_THUNDER', 'ORLANDO_MAGIC', 'PHILADELPHIA_76ERS', 'PHOENIX_SUNS', 'PORTLAND_TRAIL_BLAZERS',
'SACRAMENTO_KINGS', 'SAN_ANTONIO_SPURS', 'TORONTO_RAPTORS', 'UTAH_JAZZ', 'WASHINGTON_WIZARDS']

data['opponent'] = data['opponent'].replace(full, abb,  regex=True)
data['team'] = data['team'].replace(full, abb,  regex=True)

data.columns = ['HOME/AWAY', 'PLAYER_NAME', 'OPPONENT', 'TEAM_ABBREVIATION', 'Fantasy_Points']

data.to_csv('training_data_bbref.csv', index = False)