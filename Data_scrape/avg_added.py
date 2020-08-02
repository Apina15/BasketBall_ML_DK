import pandas as pd 

data = pd.read_csv('player_avg.csv')
boxscores = pd.read_csv('training_data_bbref.csv')

data = data.drop(['Team'], axis=1)

avg_added = boxscores.merge(data, left_on='PLAYER_NAME', right_on='Player')

avg_added = avg_added.drop(['Player'], axis=1)

avg_added['USG'] = avg_added['USG'].replace('%', '', regex=True)

avg_added['PLAYER_NAME'] = avg_added['ID']

avg_added = avg_added.drop(['ID'], axis=1)



avg_added.to_csv("training_data_bbref.csv",index=False)