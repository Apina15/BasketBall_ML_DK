# API to get data from basketball reference
from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import Team
from basketball_reference_web_scraper.data import OutputType

import pandas as pd 

# Library to get the range of a date 
import datetime as dt

# How to get the date from timestamp 
# temp = temp.strftime("%d-%b-%Y (%H:%M:%S.%f)")

# Getting the range of days from the start of the season until the postpone date
# pd.date_range(start = "2019-10-22", end = datetime.now())
dates_range_ = pd.date_range(start = "2019-10-22", end = "2019-10-23")

loop = True

# The desired data from basketball refrence we want
Total_data = pd.DataFrame(columns=['assists', 'attempted_field_goals', 'attempted_free_throws', 'attempted_three_point_field_goals', 'blocks', 
        'defensive_rebounds', 'game_score', 'location', 'made_field_goals', 'made_free_throws', 'made_three_point_field_goals', 
        'name', 'offensive_rebounds', 'opponent', 'outcome', 'personal_fouls', 'seconds_played', 'slug', 'steals', 'team', 'turnovers'])

for n in range(len(dates_range_)):
    # Setting the day, month, and year
    Day = dates_range_[n].strftime("%d")
    Month = dates_range_[n].strftime("%m")    
    Year = dates_range_[n].strftime("%Y")
    
    # Downloading the data with the API
    download_list = client.player_box_scores(day = Day, month = Month, year = Year)

    # Setting the data in the form of columns we want
    day_box_score = pd.DataFrame(download_list, columns=['assists', 'attempted_field_goals', 'attempted_free_throws', 'attempted_three_point_field_goals', 'blocks', 
        'defensive_rebounds', 'game_score', 'location', 'made_field_goals', 'made_free_throws', 'made_three_point_field_goals', 
        'name', 'offensive_rebounds', 'opponent', 'outcome', 'personal_fouls', 'seconds_played', 'slug', 'steals', 'team', 'turnovers'])

    # Adding the new day's boxscore into the data frame with all of the data
    Total_data = Total_data.append(day_box_score)


Total_data.to_csv("Current_box_scores.csv", index=False)