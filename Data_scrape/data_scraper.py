from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import Team
from basketball_reference_web_scraper.data import OutputType

import pandas as pd 

# current data 11/12

months = [10,11,12,1,2,3,4]
oct = range(22, 32)
# nov = range(1, 30)
# dec = range(1, 31)
# jan = range(1, 31)
# feb = range(1, 29)
# mar = range(1, 31)
apr = range(1, 16)

d_tn = range(1, 30)
d_t = range(1, 31)
d_to = range(1, 32)

current_m = 1
current_d = 30

i = 0
d = 0
m = oct
# print(m[len(m)-1])
loop = True

df_total = pd.DataFrame(columns=['assists', 'attempted_field_goals', 'attempted_free_throws', 'attempted_three_point_field_goals', 'blocks', 
        'defensive_rebounds', 'game_score', 'location', 'made_field_goals', 'made_free_throws', 'made_three_point_field_goals', 
        'name', 'offensive_rebounds', 'opponent', 'outcome', 'personal_fouls', 'seconds_played', 'slug', 'steals', 'team', 'turnovers'])

while(loop):
    
    print(months[i], ' Month')
    print(m[d], ' day')

    list_ = client.player_box_scores(day=m[d], month=months[i], year=2019)
    df = pd.DataFrame(list_, columns=['assists', 'attempted_field_goals', 'attempted_free_throws', 'attempted_three_point_field_goals', 'blocks', 
        'defensive_rebounds', 'game_score', 'location', 'made_field_goals', 'made_free_throws', 'made_three_point_field_goals', 
        'name', 'offensive_rebounds', 'opponent', 'outcome', 'personal_fouls', 'seconds_played', 'slug', 'steals', 'team', 'turnovers'])

    # print(df)


    df_total = df_total.append(df)

    # print(df_total)

    if (months[i] == current_m):
        if (m[d] == current_d):
            loop=False
    if(m[d] == m[len(m)-1]):
        i+=1
        d=-1
        if(i==1 or i == 2 or i == 5):
            m = d_to
        
    # print(len(m))
    d+=1


df_total.to_csv("Current_box_scores.csv", index=False)