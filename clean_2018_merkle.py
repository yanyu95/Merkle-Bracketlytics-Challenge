import pandas as pd 

# Importing the dataset
org_data = pd.read_csv('2018TeamStats Final.csv')
#add a feature to identify home/away/neutral game
#Throughout observation the away team is on even rows and home team is on odd row. If it's a neutral game, we will take care of it later
#set all games to 1(home), and then odd rows to 0 (away). 
org_data['home'] = 1
#set even rows to away in general
org_data.iloc[::2,47] = 0
data = org_data.copy()

tmp_index = data.index[(data['Team'] == 'valparaiso') & (data['PTS'] == 77) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'valparaiso') & (data['PTS'] == 79) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'grand-canyon') & (data['PTS'] == 100) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'alabama') & (data['PTS'] == 71) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'alabama') & (data['PTS'] == 80) & (data['Opp PTS'] == 79)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'princeton') & (data['PTS'] == 64) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'syracuse') & (data['PTS'] == 72) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'new-mexico-state') & (data['PTS'] == 74) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'new-mexico-state') & (data['PTS'] == 69) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'new-mexico-state') & (data['PTS'] == 63) & (data['Opp PTS'] == 54)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'baylor') & (data['PTS'] == 70) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'baylor') & (data['PTS'] == 65) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'weber-state') & (data['PTS'] == 73) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'hartford') & (data['PTS'] == 68) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'southern-methodist') & (data['PTS'] == 66) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'louisville') & (data['PTS'] == 81) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'jacksonville-state') & (data['PTS'] == 86) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'southeast-missouri-state') & (data['PTS'] == 74) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'buffalo') & (data['PTS'] == 96) & (data['Opp PTS'] == 91)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'cal-poly') & (data['PTS'] == 73) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'south-alabama') & (data['PTS'] == 68) & (data['Opp PTS'] == 46)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'south-alabama') & (data['PTS'] == 54) & (data['Opp PTS'] == 49)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'manhattan') & (data['PTS'] == 70) & (data['Opp PTS'] == 54)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'manhattan') & (data['PTS'] == 63) & (data['Opp PTS'] == 61)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'georgia-southern') & (data['PTS'] == 74) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'georgia-southern') & (data['PTS'] == 78) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'miami-fl') & (data['PTS'] == 57) & (data['Opp PTS'] == 46)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'miami-fl') & (data['PTS'] == 80) & (data['Opp PTS'] == 52)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'miami-fl') & (data['PTS'] == 84) & (data['Opp PTS'] == 81)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-arlington') & (data['PTS'] == 89) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'delaware') & (data['PTS'] == 65) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'xavier') & (data['PTS'] == 83) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'canisius') & (data['PTS'] == 68) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'canisius') & (data['PTS'] == 81) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'drexel') & (data['PTS'] == 84) & (data['Opp PTS'] == 80)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'sacred-heart') & (data['PTS'] == 69) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'fresno-state') & (data['PTS'] == 79) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'arkansas') & (data['PTS'] == 92) & (data['Opp PTS'] == 83)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'arkansas') & (data['PTS'] == 102) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'arkansas') & (data['PTS'] == 88) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'missouri') & (data['PTS'] == 95) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'missouri') & (data['PTS'] == 90) & (data['Opp PTS'] == 82)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'san-diego-state') & (data['PTS'] == 89) & (data['Opp PTS'] == 52)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'san-diego-state') & (data['PTS'] == 75) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'cal-state-bakersfield') & (data['PTS'] == 64) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'abilene-christian') & (data['PTS'] == 88) & (data['Opp PTS'] == 83)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'florida') & (data['PTS'] == 108) & (data['Opp PTS'] == 87)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'florida') & (data['PTS'] == 111) & (data['Opp PTS'] == 105)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'florida') & (data['PTS'] == 66) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'seton-hall') & (data['PTS'] == 72) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'seton-hall') & (data['PTS'] == 89) & (data['Opp PTS'] == 79)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'ucla') & (data['PTS'] == 72) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'ucla') & (data['PTS'] == 83) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'virginia-commonwealth') & (data['PTS'] == 83) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'auburn') & (data['PTS'] == 83) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'auburn') & (data['PTS'] == 89) & (data['Opp PTS'] == 78)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'auburn') & (data['PTS'] == 76) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'iona') & (data['PTS'] == 80) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'western-carolina') & (data['PTS'] == 82) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'western-carolina') & (data['PTS'] == 76) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'prairie-view') & (data['PTS'] == 80) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'prairie-view') & (data['PTS'] == 71) & (data['Opp PTS'] == 56)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'missouri-state') & (data['PTS'] == 69) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'missouri-state') & (data['PTS'] == 71) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'missouri-state') & (data['PTS'] == 73) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'wofford') & (data['PTS'] == 70) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kentucky') & (data['PTS'] == 93) & (data['Opp PTS'] == 76)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'duquesne') & (data['PTS'] == 67) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'montana-state') & (data['PTS'] == 74) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'montana-state') & (data['PTS'] == 88) & (data['Opp PTS'] == 82)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'iowa') & (data['PTS'] == 95) & (data['Opp PTS'] == 85)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'iowa') & (data['PTS'] == 90) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'iowa') & (data['PTS'] == 80) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-carolina') & (data['PTS'] == 102) & (data['Opp PTS'] == 78)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-carolina') & (data['PTS'] == 87) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-carolina') & (data['PTS'] == 85) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-carolina') & (data['PTS'] == 86) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'saint-peters') & (data['PTS'] == 70) & (data['Opp PTS'] == 61)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'saint-peters') & (data['PTS'] == 71) & (data['Opp PTS'] == 56)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'florida-state') & (data['PTS'] == 67) & (data['Opp PTS'] == 43)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'florida-state') & (data['PTS'] == 90) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'florida-state') & (data['PTS'] == 72) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'west-virginia') & (data['PTS'] == 84) & (data['Opp PTS'] == 78)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'west-virginia') & (data['PTS'] == 83) & (data['Opp PTS'] == 45)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'west-virginia') & (data['PTS'] == 83) & (data['Opp PTS'] == 79)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'eastern-washington') & (data['PTS'] == 83) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'western-kentucky') & (data['PTS'] == 77) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'western-kentucky') & (data['PTS'] == 63) & (data['Opp PTS'] == 61)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'california-santa-barbara') & (data['PTS'] == 80) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kansas') & (data['PTS'] == 65) & (data['Opp PTS'] == 61)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kansas') & (data['PTS'] == 76) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kansas') & (data['PTS'] == 75) & (data['Opp PTS'] == 54)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'ohio-state') & (data['PTS'] == 79) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'long-beach-state') & (data['PTS'] == 74) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'davidson') & (data['PTS'] == 91) & (data['Opp PTS'] == 78)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-tech') & (data['PTS'] == 75) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-tech') & (data['PTS'] == 85) & (data['Opp PTS'] == 49)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'utah') & (data['PTS'] == 83) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'utah') & (data['PTS'] == 77) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'california-davis') & (data['PTS'] == 64) & (data['Opp PTS'] == 47)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'california-davis') & (data['PTS'] == 77) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'gonzaga') & (data['PTS'] == 86) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'gonzaga') & (data['PTS'] == 76) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-am') & (data['PTS'] == 72) & (data['Opp PTS'] == 55)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-am') & (data['PTS'] == 98) & (data['Opp PTS'] == 87)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'south-dakota-state') & (data['PTS'] == 80) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'south-dakota-state') & (data['PTS'] == 94) & (data['Opp PTS'] == 80)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'rider') & (data['PTS'] == 90) & (data['Opp PTS'] == 82)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'rider') & (data['PTS'] == 94) & (data['Opp PTS'] == 80)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas') & (data['PTS'] == 61) & (data['Opp PTS'] == 48)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas') & (data['PTS'] == 66) & (data['Opp PTS'] == 50)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'southern-illinois') & (data['PTS'] == 74) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'idaho') & (data['PTS'] == 69) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'idaho') & (data['PTS'] == 75) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'radford') & (data['PTS'] == 66) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'radford') & (data['PTS'] == 72) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'middle-tennessee') & (data['PTS'] == 69) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'saint-marys-ca') & (data['PTS'] == 89) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'illinois') & (data['PTS'] == 70) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'st-johns-ny') & (data['PTS'] == 82) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'st-johns-ny') & (data['PTS'] == 46) & (data['Opp PTS'] == 43)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'st-johns-ny') & (data['PTS'] == 68) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'st-johns-ny') & (data['PTS'] == 77) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'arizona-state') & (data['PTS'] == 92) & (data['Opp PTS'] == 90)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'arizona-state') & (data['PTS'] == 102) & (data['Opp PTS'] == 86)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'arizona-state') & (data['PTS'] == 82) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'boston-college') & (data['PTS'] == 82) & (data['Opp PTS'] == 61)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'coastal-carolina') & (data['PTS'] == 83) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'coastal-carolina') & (data['PTS'] == 89) & (data['Opp PTS'] == 84)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'colorado') & (data['PTS'] == 70) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'colorado') & (data['PTS'] == 86) & (data['Opp PTS'] == 81)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'colorado') & (data['PTS'] == 79) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'california-irvine') & (data['PTS'] == 77) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'california-irvine') & (data['PTS'] == 67) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'fairfield') & (data['PTS'] == 75) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'fairfield') & (data['PTS'] == 76) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'rhode-island') & (data['PTS'] == 75) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'minnesota') & (data['PTS'] == 69) & (data['Opp PTS'] == 51)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'minnesota') & (data['PTS'] == 89) & (data['Opp PTS'] == 84)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'tennessee-tech') & (data['PTS'] == 86) & (data['Opp PTS'] == 85)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'tennessee-tech') & (data['PTS'] == 90) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-carolina-at') & (data['PTS'] == 74) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'maryland-eastern-shore') & (data['PTS'] == 66) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'dayton') & (data['PTS'] == 79) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'georgia-state') & (data['PTS'] == 68) & (data['Opp PTS'] == 50)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'northern-colorado') & (data['PTS'] == 80) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'northern-colorado') & (data['PTS'] == 63) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'northern-colorado') & (data['PTS'] == 77) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'tennessee') & (data['PTS'] == 78) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'tennessee') & (data['PTS'] == 67) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'savannah-state') & (data['PTS'] == 101) & (data['Opp PTS'] == 97)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'vermont') & (data['PTS'] == 65) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'vermont') & (data['PTS'] == 80) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'vermont') & (data['PTS'] == 66) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kent-state') & (data['PTS'] == 111) & (data['Opp PTS'] == 78)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'wichita-state') & (data['PTS'] == 92) & (data['Opp PTS'] == 82)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'wichita-state') & (data['PTS'] == 80) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'penn-state') & (data['PTS'] == 85) & (data['Opp PTS'] == 54)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'oklahoma-state') & (data['PTS'] == 73) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'oklahoma-state') & (data['PTS'] == 71) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'clemson') & (data['PTS'] == 81) & (data['Opp PTS'] == 76)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'clemson') & (data['PTS'] == 78) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'clemson') & (data['PTS'] == 71) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'hofstra') & (data['PTS'] == 72) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'central-michigan') & (data['PTS'] == 71) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'central-michigan') & (data['PTS'] == 56) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'central-michigan') & (data['PTS'] == 75) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'ohio') & (data['PTS'] == 96) & (data['Opp PTS'] == 94)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'southern-california') & (data['PTS'] == 84) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'southern-california') & (data['PTS'] == 89) & (data['Opp PTS'] == 84)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'southern-california') & (data['PTS'] == 77) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'nevada-las-vegas') & (data['PTS'] == 95) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'nevada-las-vegas') & (data['PTS'] == 85) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'nevada-las-vegas') & (data['PTS'] == 92) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'nevada-las-vegas') & (data['PTS'] == 89) & (data['Opp PTS'] == 82)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'purdue') & (data['PTS'] == 89) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'purdue') & (data['PTS'] == 82) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'binghamton') & (data['PTS'] == 70) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-dakota') & (data['PTS'] == 80) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'portland') & (data['PTS'] == 80) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'la-salle') & (data['PTS'] == 58) & (data['Opp PTS'] == 54)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'long-island-university') & (data['PTS'] == 86) & (data['Opp PTS'] == 84)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'missouri-kansas-city') & (data['PTS'] == 74) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-state') & (data['PTS'] == 71) & (data['Opp PTS'] == 54)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'drake') & (data['PTS'] == 77) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'drake') & (data['PTS'] == 90) & (data['Opp PTS'] == 88)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'western-michigan') & (data['PTS'] == 86) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'hampton') & (data['PTS'] == 76) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'mount-st-marys') & (data['PTS'] == 84) & (data['Opp PTS'] == 81)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'harvard') & (data['PTS'] == 77) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-dakota-state') & (data['PTS'] == 100) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'south-carolina-upstate') & (data['PTS'] == 88) & (data['Opp PTS'] == 78)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'louisiana-tech') & (data['PTS'] == 77) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'louisiana-tech') & (data['PTS'] == 63) & (data['Opp PTS'] == 61)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'louisiana-tech') & (data['PTS'] == 74) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'louisiana-tech') & (data['PTS'] == 85) & (data['Opp PTS'] == 76)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'cincinnati') & (data['PTS'] == 73) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'cincinnati') & (data['PTS'] == 75) & (data['Opp PTS'] == 48)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'cincinnati') & (data['PTS'] == 78) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'depaul') & (data['PTS'] == 82) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'boise-state') & (data['PTS'] == 58) & (data['Opp PTS'] == 56)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'boise-state') & (data['PTS'] == 82) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'temple') & (data['PTS'] == 76) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'temple') & (data['PTS'] == 88) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'temple') & (data['PTS'] == 67) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'temple') & (data['PTS'] == 76) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'miami-oh') & (data['PTS'] == 78) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'ipfw') & (data['PTS'] == 75) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'tulane') & (data['PTS'] == 80) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'tulane') & (data['PTS'] == 63) & (data['Opp PTS'] == 55)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'wyoming') & (data['PTS'] == 77) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'wyoming') & (data['PTS'] == 70) & (data['Opp PTS'] == 61)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'robert-morris') & (data['PTS'] == 75) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'michigan') & (data['PTS'] == 68) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'michigan') & (data['PTS'] == 90) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'navy') & (data['PTS'] == 85) & (data['Opp PTS'] == 76)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'navy') & (data['PTS'] == 79) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-san-antonio') & (data['PTS'] == 90) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'maryland') & (data['PTS'] == 80) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'bradley') & (data['PTS'] == 71) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'bradley') & (data['PTS'] == 70) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'detroit-mercy') & (data['PTS'] == 116) & (data['Opp PTS'] == 109)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'elon') & (data['PTS'] == 95) & (data['Opp PTS'] == 87)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'providence') & (data['PTS'] == 77) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'providence') & (data['PTS'] == 90) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'south-dakota') & (data['PTS'] == 84) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'south-dakota') & (data['PTS'] == 81) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'jackson-state') & (data['PTS'] == 75) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'old-dominion') & (data['PTS'] == 62) & (data['Opp PTS'] == 44)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'old-dominion') & (data['PTS'] == 75) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'old-dominion') & (data['PTS'] == 61) & (data['Opp PTS'] == 50)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'washington-state') & (data['PTS'] == 75) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'washington-state') & (data['PTS'] == 84) & (data['Opp PTS'] == 79)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'washington-state') & (data['PTS'] == 93) & (data['Opp PTS'] == 86)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'bowling-green-state') & (data['PTS'] == 83) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'richmond') & (data['PTS'] == 63) & (data['Opp PTS'] == 50)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'arizona') & (data['PTS'] == 67) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'northern-kentucky') & (data['PTS'] == 87) & (data['Opp PTS'] == 78)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'northern-kentucky') & (data['PTS'] == 85) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'notre-dame') & (data['PTS'] == 92) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'notre-dame') & (data['PTS'] == 67) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kansas-state') & (data['PTS'] == 67) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kansas-state') & (data['PTS'] == 68) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'san-francisco') & (data['PTS'] == 66) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'troy') & (data['PTS'] == 81) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'indiana') & (data['PTS'] == 80) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'northwestern') & (data['PTS'] == 82) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'oregon-state') & (data['PTS'] == 65) & (data['Opp PTS'] == 46)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'oregon-state') & (data['PTS'] == 63) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'george-washington') & (data['PTS'] == 71) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'pittsburgh') & (data['PTS'] == 76) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'wake-forest') & (data['PTS'] == 72) & (data['Opp PTS'] == 55)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'towson') & (data['PTS'] == 76) & (data['Opp PTS'] == 52)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'towson') & (data['PTS'] == 79) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'towson') & (data['PTS'] == 70) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'towson') & (data['PTS'] == 67) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'towson') & (data['PTS'] == 56) & (data['Opp PTS'] == 55)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'loyola-il') & (data['PTS'] == 102) & (data['Opp PTS'] == 78)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'loyola-il') & (data['PTS'] == 75) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-christian') & (data['PTS'] == 69) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-christian') & (data['PTS'] == 89) & (data['Opp PTS'] == 79)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-christian') & (data['PTS'] == 84) & (data['Opp PTS'] == 80)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'georgia') & (data['PTS'] == 83) & (data['Opp PTS'] == 81)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'duke') & (data['PTS'] == 88) & (data['Opp PTS'] == 81)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'duke') & (data['PTS'] == 99) & (data['Opp PTS'] == 81)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'duke') & (data['PTS'] == 85) & (data['Opp PTS'] == 78)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'duke') & (data['PTS'] == 87) & (data['Opp PTS'] == 84)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'central-florida') & (data['PTS'] == 68) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'mercer') & (data['PTS'] == 78) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'saint-josephs') & (data['PTS'] == 74) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'furman') & (data['PTS'] == 78) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'furman') & (data['PTS'] == 78) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'virginia-tech') & (data['PTS'] == 103) & (data['Opp PTS'] == 79)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'nicholls-state') & (data['PTS'] == 76) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'evansville') & (data['PTS'] == 59) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'appalachian-state') & (data['PTS'] == 76) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'northern-iowa') & (data['PTS'] == 61) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'northern-iowa') & (data['PTS'] == 64) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'denver') & (data['PTS'] == 60) & (data['Opp PTS'] == 50)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'illinois-state') & (data['PTS'] == 69) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'illinois-state') & (data['PTS'] == 84) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'college-of-charleston') & (data['PTS'] == 59) & (data['Opp PTS'] == 49)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'nevada') & (data['PTS'] == 86) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'oklahoma') & (data['PTS'] == 93) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'oklahoma') & (data['PTS'] == 90) & (data['Opp PTS'] == 80)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'oklahoma') & (data['PTS'] == 85) & (data['Opp PTS'] == 83)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'brigham-young') & (data['PTS'] == 68) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'brigham-young') & (data['PTS'] == 74) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'utah-state') & (data['PTS'] == 77) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'liberty') & (data['PTS'] == 87) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'seattle') & (data['PTS'] == 102) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'creighton') & (data['PTS'] == 100) & (data['Opp PTS'] == 89)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'saint-louis') & (data['PTS'] == 77) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'michigan-state') & (data['PTS'] == 73) & (data['Opp PTS'] == 51)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'michigan-state') & (data['PTS'] == 77) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'michigan-state') & (data['PTS'] == 63) & (data['Opp PTS'] == 45)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'michigan-state') & (data['PTS'] == 86) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'marquette') & (data['PTS'] == 94) & (data['Opp PTS'] == 83)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'marquette') & (data['PTS'] == 94) & (data['Opp PTS'] == 84)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'connecticut') & (data['PTS'] == 71) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'howard') & (data['PTS'] == 80) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'louisiana-state') & (data['PTS'] == 77) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'sam-houston-state') & (data['PTS'] == 73) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'southeastern-louisiana') & (data['PTS'] == 73) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'south-carolina') & (data['PTS'] == 80) & (data['Opp PTS'] == 56)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'south-carolina') & (data['PTS'] == 79) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'virginia') & (data['PTS'] == 68) & (data['Opp PTS'] == 42)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'virginia') & (data['PTS'] == 70) & (data['Opp PTS'] == 55)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'nebraska') & (data['PTS'] == 84) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'nebraska') & (data['PTS'] == 85) & (data['Opp PTS'] == 80)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'presbyterian') & (data['PTS'] == 75) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'mississippi') & (data['PTS'] == 79) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'portland-state') & (data['PTS'] == 83) & (data['Opp PTS'] == 79)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'portland-state') & (data['PTS'] == 87) & (data['Opp PTS'] == 78)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'louisiana-lafayette') & (data['PTS'] == 80) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'louisiana-lafayette') & (data['PTS'] == 82) & (data['Opp PTS'] == 76)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'army') & (data['PTS'] == 81) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'army') & (data['PTS'] == 82) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'army') & (data['PTS'] == 79) & (data['Opp PTS'] == 54)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'st-bonaventure') & (data['PTS'] == 63) & (data['Opp PTS'] == 61)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'st-bonaventure') & (data['PTS'] == 81) & (data['Opp PTS'] == 79)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'pennsylvania') & (data['PTS'] == 93) & (data['Opp PTS'] == 80)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'pennsylvania') & (data['PTS'] == 68) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'washington') & (data['PTS'] == 74) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'iowa-state') & (data['PTS'] == 104) & (data['Opp PTS'] == 98)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'iowa-state') & (data['PTS'] == 80) & (data['Opp PTS'] == 78)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'iowa-state') & (data['PTS'] == 75) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'iowa-state') & (data['PTS'] == 76) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'oregon') & (data['PTS'] == 89) & (data['Opp PTS'] == 79)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'montana') & (data['PTS'] == 69) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'southern-mississippi') & (data['PTS'] == 71) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'northern-illinois') & (data['PTS'] == 70) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'butler') & (data['PTS'] == 71) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'butler') & (data['PTS'] == 67) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'tulsa') & (data['PTS'] == 81) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'tulsa') & (data['PTS'] == 61) & (data['Opp PTS'] == 54)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'villanova') & (data['PTS'] == 104) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'villanova') & (data['PTS'] == 66) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'villanova') & (data['PTS'] == 85) & (data['Opp PTS'] == 76)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'villanova') & (data['PTS'] == 64) & (data['Opp PTS'] == 50)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'villanova') & (data['PTS'] == 88) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'villanova') & (data['PTS'] == 95) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'mississippi-state') & (data['PTS'] == 70) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'jacksonville') & (data['PTS'] == 92) & (data['Opp PTS'] == 84)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'jacksonville') & (data['PTS'] == 106) & (data['Opp PTS'] == 99)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'houston') & (data['PTS'] == 78) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'houston') & (data['PTS'] == 70) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)

data.to_csv('2018dataHasHome.csv')
