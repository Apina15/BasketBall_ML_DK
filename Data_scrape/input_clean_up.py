import pandas as pd
import numpy as np

data = pd.read_csv('input.csv')

data = data.drop(['Position', 'Name + ID', 'ID', 'Roster Position', 'Salary', 'AvgPointsPerGame'], axis=1)

data.columns = ['PLAYER_NAME', 'MATCHUP', 'TEAM_ABBREVIATION']

data['MATCHUP'] = data['MATCHUP'].str[:7]

data['OPPONENT'] = data['MATCHUP'].replace(data['TEAM_ABBREVIATION'], '', regex=True)
data['OPPONENT'] = data['OPPONENT'].replace('@', '', regex=True)
data['OPPONENT'] = data['OPPONENT'].replace(' ', '', regex=True)




data['HOME/AWAY'] = data['MATCHUP'].replace(data['OPPONENT'], '', regex=True)
data['HOME/AWAY'] = data['HOME/AWAY'].replace('@'+data['TEAM_ABBREVIATION'], 'Home', regex=True)
data['HOME/AWAY'] = data['HOME/AWAY'].replace(data['TEAM_ABBREVIATION']+'@', 'Away', regex=True)
data['HOME/AWAY'] = data['HOME/AWAY'].replace(' ', '', regex=True)

data = data.drop(['MATCHUP'], axis=1)

# data['Fantasy_Points'] = ""

player_avg = pd.read_csv('player_avg.csv')
player_avg = player_avg.drop(['Team'], axis=1)
avg_added = data.merge(player_avg, left_on='PLAYER_NAME', right_on='Player')
avg_added = avg_added.drop(['Player'], axis=1)
avg_added['USG'] = avg_added['USG'].replace('%', '', regex=True)
avg_added['PLAYER_NAME'] = avg_added['ID']
avg_added = avg_added.drop(['ID'], axis=1)

avg_added.to_csv('Testing_data.csv', index=False)
