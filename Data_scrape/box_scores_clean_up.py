# Names of players 

# Bojan Bogdanović - Bojan BogdanoviÄ‡
# Dario Saric - Dario Å ariÄ‡
# Tomas Satoransky - TomÃ¡Å¡ SatoranskÃ½
# Dennis Schroder - Dennis SchrÃ¶der
# Skal Labissiere - Skal LabissiÃ¨re
# Nicolo Melli - NicolÃ² Melli
# Kristaps Porzingis - Kristaps PorziÅ†Ä£is
# Jonas Valanciunas - Jonas ValanÄiÅ«nas
# Nikola Vucevic - Nikola VuÄeviÄ‡
# Nikola Jokic - Nikola JokiÄ‡
# Boban Marjanovic - Boban MarjanoviÄ‡
# Vlatko Cancar - Vlatko ÄŒanÄar
# Goran	Dragic - Goran DragiÄ‡
# Luka Doncic - Luka DonÄiÄ‡
# Juancho Hernangomez - Juan HernangÃ³mez
# Willy Hernangomez - Willy HernangÃ³mez
# Ersan Ilyasova - Ersan Ä°lyasova

import pandas as pd 

df = pd.read_csv("Current_box_scores.csv")

bad_names = ['Bojan Bogdanović', 'Dennis Schröder', 'Skal Labissière', 'Nicolò Melli', 'Kristaps Porziņģis',
            'Nikola Jokić', 'Boban Marjanović', 'Goran Dragić',
            'Juan Hernangómez', 'Willy Hernangómez', 'Ersan İlyasova', 'Bogdan Bogdanović']

good_names = ['Bojan Bogdanovic', 'Dennis Schroder', 'Skal Labissiere', 'Nicolo Melli', 'Kristaps Porzingis',
            'Nikola Jokic', 'Boban Marjanovic', 'Goran Dragic', 'Juancho Hernangomez',
            'Willy Hernangomez', 'Ersan Ilyasova', 'Bogdan Bogdanovic']

df['name'] = df['name'].replace(bad_names, good_names,  regex=True)

df.loc[df['name'].str.contains('Luka'), 'name'] = 'Luka Doncic'
df.loc[df['name'].str.contains('Dario'), 'name'] = 'Dario Saric'
df.loc[df['name'].str.contains('Jonas'), 'name'] = 'Jonas Valanciunas'
df.loc[df['name'].str.contains('Vlatko'), 'name'] = 'Vlatko Cancar'
df.loc[df['name'].str.contains('Nikola Vu'), 'name'] = 'Nikola Vucevic'
df.loc[df['name'].str.contains('Jakob'), 'name'] = 'Jakob Poeltl'
df.loc[df['name'].str.contains('Jakob'), 'name'] = 'Jakob Poeltl'
df.loc[df['name'].str.contains('Tom'), 'name'] = 'Tomas Satoransky'
df.loc[df['name'].str.contains('vis Bert'), 'name'] = 'Davis Bertans'
df.loc[df['name'].str.contains('Musa'), 'name'] = 'Dzanan Musa'

df.to_csv('no_bad_names.csv', index=False)