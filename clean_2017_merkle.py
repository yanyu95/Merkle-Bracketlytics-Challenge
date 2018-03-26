import pandas as pd 

# Importing the dataset
org_data = pd.read_csv('2017TeamStats Test.csv')
#add a feature to identify home/away/neutral game
#Throughout observation the away team is on even rows and home team is on odd row. If it's a neutral game, we will take care of it later
#set all games to 1(home), and then odd rows to 0 (away). 
org_data['home'] = 1
#set even rows to away in general
org_data.iloc[::2,47] = 0
data = org_data.copy()
data.loc[11680:,'home'] = 0

tmp_index = data.index[(data['Team'] == 'new-mexico') & (data['PTS'] == 105) & (data['Opp PTS'] == 89)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'central-florida') & (data['PTS'] == 84) & (data['Opp PTS'] == 54)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'michigan-state') & (data['PTS'] == 73) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'michigan-state') & (data['PTS'] == 77) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'michigan-state') & (data['PTS'] == 78) & (data['Opp PTS'] == 51)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'middle-tennessee') & (data['PTS'] == 68) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'middle-tennessee') & (data['PTS'] == 73) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'middle-tennessee') & (data['PTS'] == 66) & (data['Opp PTS'] == 55)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'middle-tennessee') & (data['PTS'] == 86) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'middle-tennessee') & (data['PTS'] == 82) & (data['Opp PTS'] == 56)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'middle-tennessee') & (data['PTS'] == 83) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'ball-state') & (data['PTS'] == 79) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'ball-state') & (data['PTS'] == 94) & (data['Opp PTS'] == 83)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'ball-state') & (data['PTS'] == 66) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'samford') & (data['PTS'] == 79) & (data['Opp PTS'] == 61)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'samford') & (data['PTS'] == 67) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kansas') & (data['PTS'] == 77) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kansas') & (data['PTS'] == 83) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kansas') & (data['PTS'] == 65) & (data['Opp PTS'] == 54)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kansas') & (data['PTS'] == 89) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'chattanooga') & (data['PTS'] == 75) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'rider') & (data['PTS'] == 69) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'clemson') & (data['PTS'] == 95) & (data['Opp PTS'] == 78)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'clemson') & (data['PTS'] == 67) & (data['Opp PTS'] == 54)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'clemson') & (data['PTS'] == 75) & (data['Opp PTS'] == 61)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'seattle') & (data['PTS'] == 81) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'seattle') & (data['PTS'] == 90) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'sacred-heart') & (data['PTS'] == 61) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'iona') & (data['PTS'] == 64) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'iona') & (data['PTS'] == 76) & (data['Opp PTS'] == 54)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'iona') & (data['PTS'] == 75) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'iona') & (data['PTS'] == 73) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'iona') & (data['PTS'] == 88) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'iona') & (data['PTS'] == 73) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-el-paso') & (data['PTS'] == 85) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-el-paso') & (data['PTS'] == 86) & (data['Opp PTS'] == 76)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'northern-arizona') & (data['PTS'] == 71) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'mississippi-state') & (data['PTS'] == 80) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'mississippi-state') & (data['PTS'] == 61) & (data['Opp PTS'] == 54)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'mississippi-state') & (data['PTS'] == 86) & (data['Opp PTS'] == 44)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'mississippi-state') & (data['PTS'] == 79) & (data['Opp PTS'] == 52)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'southern-illinois') & (data['PTS'] == 55) & (data['Opp PTS'] == 50)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'arizona-state') & (data['PTS'] == 80) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'arizona-state') & (data['PTS'] == 98) & (data['Opp PTS'] == 88)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'hofstra') & (data['PTS'] == 92) & (data['Opp PTS'] == 90)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'hofstra') & (data['PTS'] == 65) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'virginia') & (data['PTS'] == 74) & (data['Opp PTS'] == 41)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'virginia') & (data['PTS'] == 63) & (data['Opp PTS'] == 52)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'virginia') & (data['PTS'] == 75) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'portland') & (data['PTS'] == 96) & (data['Opp PTS'] == 78)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'portland') & (data['PTS'] == 85) & (data['Opp PTS'] == 82)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'portland') & (data['PTS'] == 53) & (data['Opp PTS'] == 45)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'portland') & (data['PTS'] == 60) & (data['Opp PTS'] == 55)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'iupui') & (data['PTS'] == 76) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'george-mason') & (data['PTS'] == 79) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'george-mason') & (data['PTS'] == 77) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'george-mason') & (data['PTS'] == 82) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-christian') & (data['PTS'] == 93) & (data['Opp PTS'] == 80)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-christian') & (data['PTS'] == 82) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-christian') & (data['PTS'] == 85) & (data['Opp PTS'] == 82)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'virginia-commonwealth') & (data['PTS'] == 75) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'virginia-commonwealth') & (data['PTS'] == 85) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'virginia-commonwealth') & (data['PTS'] == 71) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'virginia-commonwealth') & (data['PTS'] == 87) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'cal-state-bakersfield') & (data['PTS'] == 77) & (data['Opp PTS'] == 54)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'cal-state-bakersfield') & (data['PTS'] == 81) & (data['Opp PTS'] == 80)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'auburn') & (data['PTS'] == 67) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'auburn') & (data['PTS'] == 74) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'butler') & (data['PTS'] == 76) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'butler') & (data['PTS'] == 69) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'butler') & (data['PTS'] == 83) & (data['Opp PTS'] == 78)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'michigan') & (data['PTS'] == 79) & (data['Opp PTS'] == 61)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'michigan') & (data['PTS'] == 76) & (data['Opp PTS'] == 54)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'michigan') & (data['PTS'] == 75) & (data['Opp PTS'] == 55)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'michigan') & (data['PTS'] == 74) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'michigan') & (data['PTS'] == 84) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'michigan') & (data['PTS'] == 71) & (data['Opp PTS'] == 56)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'coastal-carolina') & (data['PTS'] == 83) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'coastal-carolina') & (data['PTS'] == 80) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'arizona') & (data['PTS'] == 65) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'arizona') & (data['PTS'] == 69) & (data['Opp PTS'] == 61)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'arizona') & (data['PTS'] == 67) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'arizona') & (data['PTS'] == 92) & (data['Opp PTS'] == 78)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'arizona') & (data['PTS'] == 86) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'arizona') & (data['PTS'] == 83) & (data['Opp PTS'] == 80)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'alabama-state') & (data['PTS'] == 76) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'fairfield') & (data['PTS'] == 89) & (data['Opp PTS'] == 83)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'loyola-il') & (data['PTS'] == 78) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'loyola-il') & (data['PTS'] == 88) & (data['Opp PTS'] == 79)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'south-carolina') & (data['PTS'] == 64) & (data['Opp PTS'] == 50)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'denver') & (data['PTS'] == 72) & (data['Opp PTS'] == 61)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'east-tennessee-state') & (data['PTS'] == 86) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'east-tennessee-state') & (data['PTS'] == 71) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'east-tennessee-state') & (data['PTS'] == 72) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'east-tennessee-state') & (data['PTS'] == 73) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'east-tennessee-state') & (data['PTS'] == 81) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'east-tennessee-state') & (data['PTS'] == 79) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'northeastern') & (data['PTS'] == 80) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'south-dakota') & (data['PTS'] == 80) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'south-dakota') & (data['PTS'] == 78) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'utah') & (data['PTS'] == 74) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'murray-state') & (data['PTS'] == 93) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'murray-state') & (data['PTS'] == 85) & (data['Opp PTS'] == 84)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'murray-state') & (data['PTS'] == 75) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'nevada') & (data['PTS'] == 82) & (data['Opp PTS'] == 78)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'nevada') & (data['PTS'] == 67) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'nevada') & (data['PTS'] == 81) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'nevada') & (data['PTS'] == 67) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'nevada') & (data['PTS'] == 83) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'nevada') & (data['PTS'] == 83) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'nevada') & (data['PTS'] == 79) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'southern-utah') & (data['PTS'] == 109) & (data['Opp PTS'] == 105)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'penn-state') & (data['PTS'] == 72) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'penn-state') & (data['PTS'] == 76) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'san-francisco') & (data['PTS'] == 77) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'san-francisco') & (data['PTS'] == 89) & (data['Opp PTS'] == 86)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'san-francisco') & (data['PTS'] == 66) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kansas-state') & (data['PTS'] == 72) & (data['Opp PTS'] == 54)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kansas-state') & (data['PTS'] == 70) & (data['Opp PTS'] == 56)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kansas-state') & (data['PTS'] == 89) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kansas-state') & (data['PTS'] == 70) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'massachusetts-lowell') & (data['PTS'] == 76) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'oklahoma') & (data['PTS'] == 89) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'oklahoma') & (data['PTS'] == 70) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'richmond') & (data['PTS'] == 67) & (data['Opp PTS'] == 54)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'richmond') & (data['PTS'] == 70) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'colorado') & (data['PTS'] == 68) & (data['Opp PTS'] == 54)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'colorado') & (data['PTS'] == 73) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'niagara') & (data['PTS'] == 88) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'monmouth') & (data['PTS'] == 86) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'monmouth') & (data['PTS'] == 84) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'stetson') & (data['PTS'] == 98) & (data['Opp PTS'] == 90)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'cornell') & (data['PTS'] == 78) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'marquette') & (data['PTS'] == 95) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-dakota-state') & (data['PTS'] == 66) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'tennessee-martin') & (data['PTS'] == 73) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-pan-american') & (data['PTS'] == 101) & (data['Opp PTS'] == 93)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-pan-american') & (data['PTS'] == 71) & (data['Opp PTS'] == 61)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'virginia-tech') & (data['PTS'] == 92) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'virginia-tech') & (data['PTS'] == 66) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'virginia-tech') & (data['PTS'] == 99) & (data['Opp PTS'] == 90)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'air-force') & (data['PTS'] == 83) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'alcorn-state') & (data['PTS'] == 81) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'james-madison') & (data['PTS'] == 80) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'illinois-chicago') & (data['PTS'] == 84) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'illinois-chicago') & (data['PTS'] == 79) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'alabama') & (data['PTS'] == 62) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'alabama') & (data['PTS'] == 67) & (data['Opp PTS'] == 52)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'alabama') & (data['PTS'] == 75) & (data['Opp PTS'] == 55)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'alabama') & (data['PTS'] == 64) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'binghamton') & (data['PTS'] == 72) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'georgia-southern') & (data['PTS'] == 83) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'georgia-southern') & (data['PTS'] == 65) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'louisville') & (data['PTS'] == 68) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'louisville') & (data['PTS'] == 62) & (data['Opp PTS'] == 52)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'louisville') & (data['PTS'] == 77) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'northwestern') & (data['PTS'] == 77) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'northwestern') & (data['PTS'] == 67) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'northwestern') & (data['PTS'] == 83) & (data['Opp PTS'] == 61)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'northwestern') & (data['PTS'] == 72) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'st-bonaventure') & (data['PTS'] == 102) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'st-bonaventure') & (data['PTS'] == 89) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'st-bonaventure') & (data['PTS'] == 79) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'st-bonaventure') & (data['PTS'] == 73) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'st-bonaventure') & (data['PTS'] == 73) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'nebraska-omaha') & (data['PTS'] == 84) & (data['Opp PTS'] == 80)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'nebraska-omaha') & (data['PTS'] == 90) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'bucknell') & (data['PTS'] == 84) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'bucknell') & (data['PTS'] == 75) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'saint-peters') & (data['PTS'] == 90) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'saint-peters') & (data['PTS'] == 84) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'saint-peters') & (data['PTS'] == 61) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'illinois-state') & (data['PTS'] == 68) & (data['Opp PTS'] == 56)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'illinois-state') & (data['PTS'] == 80) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'illinois-state') & (data['PTS'] == 63) & (data['Opp PTS'] == 50)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'boston-college') & (data['PTS'] == 72) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'pittsburgh') & (data['PTS'] == 78) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'pittsburgh') & (data['PTS'] == 81) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'pittsburgh') & (data['PTS'] == 61) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'duke') & (data['PTS'] == 78) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'duke') & (data['PTS'] == 75) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'duke') & (data['PTS'] == 84) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'duke') & (data['PTS'] == 94) & (data['Opp PTS'] == 45)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'duke') & (data['PTS'] == 72) & (data['Opp PTS'] == 61)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'duke') & (data['PTS'] == 79) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'duke') & (data['PTS'] == 81) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'duke') & (data['PTS'] == 93) & (data['Opp PTS'] == 83)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'duke') & (data['PTS'] == 75) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'fresno-state') & (data['PTS'] == 65) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'south-carolina-state') & (data['PTS'] == 82) & (data['Opp PTS'] == 78)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'marist') & (data['PTS'] == 87) & (data['Opp PTS'] == 79)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'towson') & (data['PTS'] == 76) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'towson') & (data['PTS'] == 82) & (data['Opp PTS'] == 54)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'villanova') & (data['PTS'] == 76) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'villanova') & (data['PTS'] == 96) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'villanova') & (data['PTS'] == 67) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'villanova') & (data['PTS'] == 89) & (data['Opp PTS'] == 79)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'villanova') & (data['PTS'] == 74) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'villanova') & (data['PTS'] == 108) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'villanova') & (data['PTS'] == 55) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'villanova') & (data['PTS'] == 74) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'vermont') & (data['PTS'] == 60) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'vermont') & (data['PTS'] == 87) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'quinnipiac') & (data['PTS'] == 80) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'west-virginia') & (data['PTS'] == 89) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'west-virginia') & (data['PTS'] == 90) & (data['Opp PTS'] == 37)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'west-virginia') & (data['PTS'] == 63) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'west-virginia') & (data['PTS'] == 51) & (data['Opp PTS'] == 50)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'wofford') & (data['PTS'] == 79) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-florida') & (data['PTS'] == 76) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'delaware') & (data['PTS'] == 81) & (data['Opp PTS'] == 76)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'portland-state') & (data['PTS'] == 80) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'wyoming') & (data['PTS'] == 72) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'santa-clara') & (data['PTS'] == 76) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'boise-state') & (data['PTS'] == 91) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'missouri') & (data['PTS'] == 67) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'missouri') & (data['PTS'] == 86) & (data['Opp PTS'] == 83)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'massachusetts') & (data['PTS'] == 68) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'massachusetts') & (data['PTS'] == 70) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'stephen-f-austin') & (data['PTS'] == 67) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'stephen-f-austin') & (data['PTS'] == 75) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'youngstown-state') & (data['PTS'] == 78) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'youngstown-state') & (data['PTS'] == 84) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'youngstown-state') & (data['PTS'] == 81) & (data['Opp PTS'] == 80)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'st-francis-ny') & (data['PTS'] == 97) & (data['Opp PTS'] == 91)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'xavier') & (data['PTS'] == 83) & (data['Opp PTS'] == 82)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'xavier') & (data['PTS'] == 83) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'xavier') & (data['PTS'] == 67) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'xavier') & (data['PTS'] == 75) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'xavier') & (data['PTS'] == 62) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'milwaukee') & (data['PTS'] == 54) & (data['Opp PTS'] == 37)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'milwaukee') & (data['PTS'] == 85) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'milwaukee') & (data['PTS'] == 43) & (data['Opp PTS'] == 41)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'milwaukee') & (data['PTS'] == 74) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'florida-state') & (data['PTS'] == 72) & (data['Opp PTS'] == 61)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'florida-state') & (data['PTS'] == 67) & (data['Opp PTS'] == 48)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'florida-state') & (data['PTS'] == 83) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'florida-state') & (data['PTS'] == 74) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-am-corpus-christi') & (data['PTS'] == 77) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'southern-california') & (data['PTS'] == 91) & (data['Opp PTS'] == 84)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'southern-california') & (data['PTS'] == 83) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'southern-california') & (data['PTS'] == 94) & (data['Opp PTS'] == 92)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'southern-california') & (data['PTS'] == 78) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'ucla') & (data['PTS'] == 99) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'ucla') & (data['PTS'] == 82) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'ucla') & (data['PTS'] == 74) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'ucla') & (data['PTS'] == 86) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'ucla') & (data['PTS'] == 76) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'old-dominion') & (data['PTS'] == 63) & (data['Opp PTS'] == 55)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'norfolk-state') & (data['PTS'] == 93) & (data['Opp PTS'] == 88)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'norfolk-state') & (data['PTS'] == 68) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'central-arkansas') & (data['PTS'] == 81) & (data['Opp PTS'] == 76)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'dayton') & (data['PTS'] == 84) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'dayton') & (data['PTS'] == 64) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'mercer') & (data['PTS'] == 70) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'sam-houston-state') & (data['PTS'] == 77) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'sam-houston-state') & (data['PTS'] == 63) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'providence') & (data['PTS'] == 60) & (data['Opp PTS'] == 51)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'louisiana-tech') & (data['PTS'] == 89) & (data['Opp PTS'] == 55)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'louisiana-tech') & (data['PTS'] == 69) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'stony-brook') & (data['PTS'] == 76) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'california') & (data['PTS'] == 62) & (data['Opp PTS'] == 51)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'california') & (data['PTS'] == 67) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'california') & (data['PTS'] == 78) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'illinois') & (data['PTS'] == 64) & (data['Opp PTS'] == 46)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'illinois') & (data['PTS'] == 75) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'illinois') & (data['PTS'] == 75) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'lamar') & (data['PTS'] == 77) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'radford') & (data['PTS'] == 80) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'radford') & (data['PTS'] == 56) & (data['Opp PTS'] == 52)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'south-carolina-upstate') & (data['PTS'] == 80) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'south-carolina-upstate') & (data['PTS'] == 71) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'njit') & (data['PTS'] == 71) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'alabama-birmingham') & (data['PTS'] == 81) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'alabama-birmingham') & (data['PTS'] == 74) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'georgetown') & (data['PTS'] == 65) & (data['Opp PTS'] == 61)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'georgetown') & (data['PTS'] == 93) & (data['Opp PTS'] == 78)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'long-island-university') & (data['PTS'] == 78) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'long-island-university') & (data['PTS'] == 71) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'long-island-university') & (data['PTS'] == 74) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'georgia') & (data['PTS'] == 81) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'georgia') & (data['PTS'] == 59) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'utah-valley') & (data['PTS'] == 65) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'brigham-young') & (data['PTS'] == 92) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'brigham-young') & (data['PTS'] == 77) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'brigham-young') & (data['PTS'] == 89) & (data['Opp PTS'] == 81)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'robert-morris') & (data['PTS'] == 62) & (data['Opp PTS'] == 48)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'robert-morris') & (data['PTS'] == 64) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'robert-morris') & (data['PTS'] == 74) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'cal-state-fullerton') & (data['PTS'] == 81) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'east-carolina') & (data['PTS'] == 70) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'east-carolina') & (data['PTS'] == 80) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'elon') & (data['PTS'] == 91) & (data['Opp PTS'] == 80)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'elon') & (data['PTS'] == 72) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'purdue') & (data['PTS'] == 85) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'purdue') & (data['PTS'] == 96) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'purdue') & (data['PTS'] == 97) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'purdue') & (data['PTS'] == 86) & (data['Opp PTS'] == 81)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'bethune-cookman') & (data['PTS'] == 69) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'st-johns-ny') & (data['PTS'] == 74) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'maryland') & (data['PTS'] == 88) & (data['Opp PTS'] == 82)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'maryland') & (data['PTS'] == 69) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'maryland') & (data['PTS'] == 88) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'tulsa') & (data['PTS'] == 74) & (data['Opp PTS'] == 51)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'tulsa') & (data['PTS'] == 66) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'california-davis') & (data['PTS'] == 89) & (data['Opp PTS'] == 76)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'california-davis') & (data['PTS'] == 81) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'california-davis') & (data['PTS'] == 64) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'california-davis') & (data['PTS'] == 66) & (data['Opp PTS'] == 55)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'california-davis') & (data['PTS'] == 66) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'california-davis') & (data['PTS'] == 50) & (data['Opp PTS'] == 47)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kent-state') & (data['PTS'] == 79) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kent-state') & (data['PTS'] == 66) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kent-state') & (data['PTS'] == 68) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kent-state') & (data['PTS'] == 68) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kent-state') & (data['PTS'] == 70) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'northern-colorado') & (data['PTS'] == 81) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'southern-methodist') & (data['PTS'] == 76) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'southern-methodist') & (data['PTS'] == 81) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'southern-methodist') & (data['PTS'] == 70) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'southern-methodist') & (data['PTS'] == 71) & (data['Opp PTS'] == 56)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'ohio') & (data['PTS'] == 67) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'mississippi') & (data['PTS'] == 95) & (data['Opp PTS'] == 88)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'mississippi') & (data['PTS'] == 81) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'mississippi') & (data['PTS'] == 86) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'iowa') & (data['PTS'] == 69) & (data['Opp PTS'] == 46)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'george-washington') & (data['PTS'] == 53) & (data['Opp PTS'] == 46)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'houston') & (data['PTS'] == 93) & (data['Opp PTS'] == 56)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'houston') & (data['PTS'] == 85) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'houston') & (data['PTS'] == 72) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'oakland') & (data['PTS'] == 79) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'new-mexico-state') & (data['PTS'] == 67) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'new-mexico-state') & (data['PTS'] == 78) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'new-mexico-state') & (data['PTS'] == 70) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'fairleigh-dickinson') & (data['PTS'] == 90) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'yale') & (data['PTS'] == 73) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'cincinnati') & (data['PTS'] == 71) & (data['Opp PTS'] == 50)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'cincinnati') & (data['PTS'] == 80) & (data['Opp PTS'] == 61)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'cincinnati') & (data['PTS'] == 81) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'northern-iowa') & (data['PTS'] == 73) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'eastern-michigan') & (data['PTS'] == 76) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'idaho') & (data['PTS'] == 81) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-carolina-central') & (data['PTS'] == 95) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-carolina-central') & (data['PTS'] == 67) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'marshall') & (data['PTS'] == 89) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'marshall') & (data['PTS'] == 64) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'marshall') & (data['PTS'] == 93) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'indiana') & (data['PTS'] == 103) & (data['Opp PTS'] == 99)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'indiana') & (data['PTS'] == 95) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'rhode-island') & (data['PTS'] == 76) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'rhode-island') & (data['PTS'] == 74) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'rhode-island') & (data['PTS'] == 84) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'rhode-island') & (data['PTS'] == 70) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'albany-ny') & (data['PTS'] == 80) & (data['Opp PTS'] == 76)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'new-orleans') & (data['PTS'] == 75) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'new-orleans') & (data['PTS'] == 68) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'grambling') & (data['PTS'] == 110) & (data['Opp PTS'] == 104)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'jacksonville') & (data['PTS'] == 79) & (data['Opp PTS'] == 54)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'jacksonville') & (data['PTS'] == 78) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'saint-louis') & (data['PTS'] == 72) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'wichita-state') & (data['PTS'] == 82) & (data['Opp PTS'] == 47)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'wichita-state') & (data['PTS'] == 76) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'wichita-state') & (data['PTS'] == 82) & (data['Opp PTS'] == 56)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'wichita-state') & (data['PTS'] == 78) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'wichita-state') & (data['PTS'] == 71) & (data['Opp PTS'] == 51)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'baylor') & (data['PTS'] == 71) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'baylor') & (data['PTS'] == 73) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'baylor') & (data['PTS'] == 66) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'baylor') & (data['PTS'] == 82) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'troy') & (data['PTS'] == 92) & (data['Opp PTS'] == 84)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'troy') & (data['PTS'] == 83) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'troy') & (data['PTS'] == 84) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'troy') & (data['PTS'] == 90) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'troy') & (data['PTS'] == 74) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'troy') & (data['PTS'] == 59) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-am') & (data['PTS'] == 95) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-am') & (data['PTS'] == 68) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'florida') & (data['PTS'] == 80) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'florida') & (data['PTS'] == 76) & (data['Opp PTS'] == 54)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'florida') & (data['PTS'] == 73) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'florida') & (data['PTS'] == 78) & (data['Opp PTS'] == 61)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'florida') & (data['PTS'] == 81) & (data['Opp PTS'] == 76)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'florida') & (data['PTS'] == 65) & (data['Opp PTS'] == 56)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'florida') & (data['PTS'] == 87) & (data['Opp PTS'] == 46)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-state') & (data['PTS'] == 61) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-state') & (data['PTS'] == 86) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-state') & (data['PTS'] == 63) & (data['Opp PTS'] == 51)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-state') & (data['PTS'] == 83) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'louisiana-monroe') & (data['PTS'] == 73) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'duquesne') & (data['PTS'] == 64) & (data['Opp PTS'] == 55)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'gonzaga') & (data['PTS'] == 82) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'gonzaga') & (data['PTS'] == 77) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'gonzaga') & (data['PTS'] == 73) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'gonzaga') & (data['PTS'] == 69) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'gonzaga') & (data['PTS'] == 86) & (data['Opp PTS'] == 76)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'gonzaga') & (data['PTS'] == 82) & (data['Opp PTS'] == 50)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'gonzaga') & (data['PTS'] == 77) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'gonzaga') & (data['PTS'] == 74) & (data['Opp PTS'] == 56)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'college-of-charleston') & (data['PTS'] == 67) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'college-of-charleston') & (data['PTS'] == 67) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'pacific') & (data['PTS'] == 89) & (data['Opp PTS'] == 84)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'william-mary') & (data['PTS'] == 71) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'oregon') & (data['PTS'] == 69) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'oregon') & (data['PTS'] == 79) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'oregon') & (data['PTS'] == 83) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'oregon') & (data['PTS'] == 80) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'oregon') & (data['PTS'] == 73) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'washington') & (data['PTS'] == 86) & (data['Opp PTS'] == 47)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'montana') & (data['PTS'] == 68) & (data['Opp PTS'] == 47)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'davidson') & (data['PTS'] == 70) & (data['Opp PTS'] == 55)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'davidson') & (data['PTS'] == 68) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'davidson') & (data['PTS'] == 82) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'davidson') & (data['PTS'] == 73) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'siena') & (data['PTS'] == 71) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'siena') & (data['PTS'] == 78) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'oklahoma-state') & (data['PTS'] == 98) & (data['Opp PTS'] == 90)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'oklahoma-state') & (data['PTS'] == 97) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-carolina') & (data['PTS'] == 95) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-carolina') & (data['PTS'] == 107) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-carolina') & (data['PTS'] == 71) & (data['Opp PTS'] == 56)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-carolina') & (data['PTS'] == 83) & (data['Opp PTS'] == 76)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-carolina') & (data['PTS'] == 78) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'grand-canyon') & (data['PTS'] == 82) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'grand-canyon') & (data['PTS'] == 84) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'maryland-eastern-shore') & (data['PTS'] == 75) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'maryland-eastern-shore') & (data['PTS'] == 68) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'san-diego-state') & (data['PTS'] == 77) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'san-diego-state') & (data['PTS'] == 66) & (data['Opp PTS'] == 51)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'san-diego-state') & (data['PTS'] == 82) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'san-diego-state') & (data['PTS'] == 62) & (data['Opp PTS'] == 48)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'san-diego-state') & (data['PTS'] == 87) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'toledo') & (data['PTS'] == 83) & (data['Opp PTS'] == 79)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'stanford') & (data['PTS'] == 80) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'stanford') & (data['PTS'] == 65) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'stanford') & (data['PTS'] == 66) & (data['Opp PTS'] == 52)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'citadel') & (data['PTS'] == 78) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-tech') & (data['PTS'] == 75) & (data['Opp PTS'] == 51)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'eastern-washington') & (data['PTS'] == 89) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'missouri-state') & (data['PTS'] == 69) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'missouri-state') & (data['PTS'] == 70) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-san-antonio') & (data['PTS'] == 56) & (data['Opp PTS'] == 52)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'utah-state') & (data['PTS'] == 90) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'connecticut') & (data['PTS'] == 52) & (data['Opp PTS'] == 50)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'creighton') & (data['PTS'] == 103) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'creighton') & (data['PTS'] == 112) & (data['Opp PTS'] == 94)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'creighton') & (data['PTS'] == 86) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'creighton') & (data['PTS'] == 70) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'creighton') & (data['PTS'] == 75) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'vanderbilt') & (data['PTS'] == 76) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'vanderbilt') & (data['PTS'] == 66) & (data['Opp PTS'] == 41)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'vanderbilt') & (data['PTS'] == 72) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'sacramento-state') & (data['PTS'] == 91) & (data['Opp PTS'] == 76)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'austin-peay') & (data['PTS'] == 77) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'austin-peay') & (data['PTS'] == 76) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'wake-forest') & (data['PTS'] == 103) & (data['Opp PTS'] == 81)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'wake-forest') & (data['PTS'] == 92) & (data['Opp PTS'] == 78)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'arkansas-state') & (data['PTS'] == 73) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'bradley') & (data['PTS'] == 70) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'bradley') & (data['PTS'] == 67) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'arkansas-little-rock') & (data['PTS'] == 68) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'arkansas-little-rock') & (data['PTS'] == 91) & (data['Opp PTS'] == 79)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'buffalo') & (data['PTS'] == 74) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'chicago-state') & (data['PTS'] == 74) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-arlington') & (data['PTS'] == 74) & (data['Opp PTS'] == 51)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'minnesota') & (data['PTS'] == 56) & (data['Opp PTS'] == 52)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'minnesota') & (data['PTS'] == 63) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'colorado-state') & (data['PTS'] == 81) & (data['Opp PTS'] == 55)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'colorado-state') & (data['PTS'] == 71) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'saint-marys-ca') & (data['PTS'] == 76) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'saint-marys-ca') & (data['PTS'] == 81) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'saint-marys-ca') & (data['PTS'] == 81) & (data['Opp PTS'] == 50)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-southern') & (data['PTS'] == 62) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas-southern') & (data['PTS'] == 53) & (data['Opp PTS'] == 50)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'wisconsin') & (data['PTS'] == 74) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'wisconsin') & (data['PTS'] == 73) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'wisconsin') & (data['PTS'] == 61) & (data['Opp PTS'] == 54)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'wisconsin') & (data['PTS'] == 70) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'wisconsin') & (data['PTS'] == 76) & (data['Opp PTS'] == 48)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'evansville') & (data['PTS'] == 83) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'rice') & (data['PTS'] == 86) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'valparaiso') & (data['PTS'] == 68) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'valparaiso') & (data['PTS'] == 92) & (data['Opp PTS'] == 89)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'missouri-kansas-city') & (data['PTS'] == 85) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'missouri-kansas-city') & (data['PTS'] == 82) & (data['Opp PTS'] == 78)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'weber-state') & (data['PTS'] == 86) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'weber-state') & (data['PTS'] == 90) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'weber-state') & (data['PTS'] == 80) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'campbell') & (data['PTS'] == 73) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'campbell') & (data['PTS'] == 81) & (data['Opp PTS'] == 79)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'campbell') & (data['PTS'] == 66) & (data['Opp PTS'] == 50)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'princeton') & (data['PTS'] == 75) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'princeton') & (data['PTS'] == 72) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'princeton') & (data['PTS'] == 71) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'california-irvine') & (data['PTS'] == 63) & (data['Opp PTS'] == 52)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'california-irvine') & (data['PTS'] == 76) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'california-irvine') & (data['PTS'] == 62) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kentucky') & (data['PTS'] == 69) & (data['Opp PTS'] == 48)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kentucky') & (data['PTS'] == 115) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kentucky') & (data['PTS'] == 96) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kentucky') & (data['PTS'] == 103) & (data['Opp PTS'] == 100)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kentucky') & (data['PTS'] == 71) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kentucky') & (data['PTS'] == 79) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'kentucky') & (data['PTS'] == 82) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'nicholls-state') & (data['PTS'] == 76) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'long-beach-state') & (data['PTS'] == 71) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'long-beach-state') & (data['PTS'] == 73) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'notre-dame') & (data['PTS'] == 89) & (data['Opp PTS'] == 83)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'notre-dame') & (data['PTS'] == 70) & (data['Opp PTS'] == 66)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'notre-dame') & (data['PTS'] == 71) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'notre-dame') & (data['PTS'] == 77) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'southeast-missouri-state') & (data['PTS'] == 78) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'central-michigan') & (data['PTS'] == 88) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'eastern-kentucky') & (data['PTS'] == 91) & (data['Opp PTS'] == 82)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'canisius') & (data['PTS'] == 94) & (data['Opp PTS'] == 87)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'canisius') & (data['PTS'] == 77) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'pepperdine') & (data['PTS'] == 66) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'iowa-state') & (data['PTS'] == 73) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'iowa-state') & (data['PTS'] == 73) & (data['Opp PTS'] == 56)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'iowa-state') & (data['PTS'] == 97) & (data['Opp PTS'] == 80)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'iowa-state') & (data['PTS'] == 92) & (data['Opp PTS'] == 83)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'iowa-state') & (data['PTS'] == 84) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'iowa-state') & (data['PTS'] == 80) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'miami-fl') & (data['PTS'] == 67) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'miami-fl') & (data['PTS'] == 74) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'miami-fl') & (data['PTS'] == 62) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'louisiana-state') & (data['PTS'] == 66) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'memphis') & (data['PTS'] == 100) & (data['Opp PTS'] == 92)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'south-dakota-state') & (data['PTS'] == 81) & (data['Opp PTS'] == 58)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'south-dakota-state') & (data['PTS'] == 83) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'south-dakota-state') & (data['PTS'] == 74) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'south-dakota-state') & (data['PTS'] == 79) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-carolina-greensboro') & (data['PTS'] == 65) & (data['Opp PTS'] == 54)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-carolina-greensboro') & (data['PTS'] == 72) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-carolina-greensboro') & (data['PTS'] == 76) & (data['Opp PTS'] == 67)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-carolina-greensboro') & (data['PTS'] == 77) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'nebraska') & (data['PTS'] == 80) & (data['Opp PTS'] == 78)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'texas') & (data['PTS'] == 61) & (data['Opp PTS'] == 52)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'bryant') & (data['PTS'] == 64) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'northwestern-state') & (data['PTS'] == 68) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'green-bay') & (data['PTS'] == 95) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'southern-illinois-edwardsville') & (data['PTS'] == 77) & (data['Opp PTS'] == 68)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'jacksonville-state') & (data['PTS'] == 61) & (data['Opp PTS'] == 38)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'jacksonville-state') & (data['PTS'] == 76) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'jacksonville-state') & (data['PTS'] == 74) & (data['Opp PTS'] == 51)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'jacksonville-state') & (data['PTS'] == 65) & (data['Opp PTS'] == 59)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'jacksonville-state') & (data['PTS'] == 66) & (data['Opp PTS'] == 55)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'saint-josephs') & (data['PTS'] == 71) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'saint-josephs') & (data['PTS'] == 78) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'gardner-webb') & (data['PTS'] == 94) & (data['Opp PTS'] == 78)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'gardner-webb') & (data['PTS'] == 91) & (data['Opp PTS'] == 55)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'louisiana-lafayette') & (data['PTS'] == 78) & (data['Opp PTS'] == 71)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'rutgers') & (data['PTS'] == 68) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'rutgers') & (data['PTS'] == 66) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'arkansas') & (data['PTS'] == 77) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'arkansas') & (data['PTS'] == 90) & (data['Opp PTS'] == 56)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'arkansas') & (data['PTS'] == 73) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'arkansas') & (data['PTS'] == 76) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'seton-hall') & (data['PTS'] == 90) & (data['Opp PTS'] == 79)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'seton-hall') & (data['PTS'] == 68) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'seton-hall') & (data['PTS'] == 60) & (data['Opp PTS'] == 57)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'seton-hall') & (data['PTS'] == 67) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'seton-hall') & (data['PTS'] == 82) & (data['Opp PTS'] == 76)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'temple') & (data['PTS'] == 89) & (data['Opp PTS'] == 86)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'temple') & (data['PTS'] == 81) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'temple') & (data['PTS'] == 74) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'northern-kentucky') & (data['PTS'] == 74) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'northern-kentucky') & (data['PTS'] == 82) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'northern-kentucky') & (data['PTS'] == 84) & (data['Opp PTS'] == 74)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'northern-kentucky') & (data['PTS'] == 59) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'georgia-state') & (data['PTS'] == 74) & (data['Opp PTS'] == 53)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'georgia-state') & (data['PTS'] == 82) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'georgia-state') & (data['PTS'] == 86) & (data['Opp PTS'] == 76)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'washington-state') & (data['PTS'] == 87) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'washington-state') & (data['PTS'] == 75) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-carolina-wilmington') & (data['PTS'] == 65) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-carolina-wilmington') & (data['PTS'] == 102) & (data['Opp PTS'] == 77)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-carolina-wilmington') & (data['PTS'] == 91) & (data['Opp PTS'] == 82)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-carolina-wilmington') & (data['PTS'] == 105) & (data['Opp PTS'] == 94)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-carolina-wilmington') & (data['PTS'] == 78) & (data['Opp PTS'] == 69)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-dakota') & (data['PTS'] == 57) & (data['Opp PTS'] == 55)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-dakota') & (data['PTS'] == 95) & (data['Opp PTS'] == 72)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-dakota') & (data['PTS'] == 69) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'north-dakota') & (data['PTS'] == 93) & (data['Opp PTS'] == 89)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'akron') & (data['PTS'] == 84) & (data['Opp PTS'] == 75)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'akron') & (data['PTS'] == 65) & (data['Opp PTS'] == 63)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'akron') & (data['PTS'] == 88) & (data['Opp PTS'] == 80)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'akron') & (data['PTS'] == 76) & (data['Opp PTS'] == 60)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'akron') & (data['PTS'] == 79) & (data['Opp PTS'] == 62)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'akron') & (data['PTS'] == 74) & (data['Opp PTS'] == 70)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'howard') & (data['PTS'] == 79) & (data['Opp PTS'] == 73)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'howard') & (data['PTS'] == 68) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'tennessee-state') & (data['PTS'] == 78) & (data['Opp PTS'] == 64)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)
tmp_index = data.index[(data['Team'] == 'tennessee-state') & (data['PTS'] == 69) & (data['Opp PTS'] == 65)].tolist()[0]
tmp_value = data.loc[tmp_index, 'home']
data.loc[tmp_index, 'home'] = abs(1-tmp_value)

#But all these games are regular season, we also need to change march madness games to zero. The index starts with 11680 
#and we also need to change the first four games
data.loc[11680:,'home'] = 0
data.loc[11675,'home'] = 0
data.loc[11674,'home'] = 0
data.loc[11671,'home'] = 0
data.loc[11670,'home'] = 0

data.to_csv('2017dataHasHome.csv')
# =============================================================================
# dataset = data.drop(['Unnamed: 0','gameid'],axis = 1)
# 
# features = list(dataset.columns.values)[2:]
# 
# #Normalize those game which have extra time to regualr time 200
# for index, row in dataset.iterrows():
#     mp = row['MP']
#     if mp > 200:
#         dataset.iloc[index, 2:-2] = dataset.iloc[index, 2:-2] * 200/mp
# #Now we can get rid of MP
# dataset = dataset.drop(['MP'],axis = 1)        
# #find all the  team
# team_names =list(set((dataset['Team'])))   
# #calculate team dictionary
# team_perf = {}
# for team in team_names:
#     temp = dataset.loc[dataset['Team'] == team]
#     need_average = temp.drop(['Win?','Team','home'],axis = 1)
#     mean = np.mean(need_average)
#     sum_win = temp['Win?'].sum()
#     mean = np.array(mean)
#     mean = np.append(mean, [sum_win])
#     a = mean.tolist()
#     a.insert(0,team)
#     team_perf[team] = a
#     
# #add new variable
# #Final four from 2007 to 2017
# F4 = pd.read_csv('TOP4(2007-2017).csv')
# dataset_F4 = F4.drop(['Rank','Year'],axis = 1)
# dataset_F4
# F4_teams = list(set(dataset_F4['Team'])) 
# F4_teams
# 
# for key, value in team_perf.items():
#     if key in F4_teams:
#         value.append(1)
#     else:
#         value.append(0)
# #
# conference = pd.read_csv('Competitive Conference.csv')
# new_conference=conference[['conference','Team name']]
# new_conference=list(set(new_conference['Team name']))
# 
# for key,value in team_perf.items():
#     if key in new_conference:
#         value.append(1)
#     else:
#         value.append(0)
#         
# 
# ####deal with player info
# from math import log
# 
# player_data = pd.read_csv('2017PlayerStats Test.csv')
# 
# dataset = player_data.drop(['Unnamed: 0','gameid'],axis = 1)
# dataset2 = player_data[['player','MP','3P','AST','FG','FT','TOV','FGA','FTA','TRB','ORB','STL','BLK','PF','PTS']]
# player_names = list(set(dataset2['player']))
# player_perf = {}
# 
# player_team = {}
# 
# 
# for player in player_names:
#     temp = dataset2.loc[dataset2['player'] == player]
#     need_average = temp.drop(['player'],axis = 1)
#     mean = np.mean(need_average)
#     mean = mean.tolist()
#     player_perf[player] = mean
#     
#     team_name = dataset.loc[dataset['player'] == player].iloc[0][-1]
#     player_team[player] = team_name
#     
# #factor = (2 / 3) - (0.5 * (lg_AST / lg_FG)) / (2 * (lg_FG / lg_FT))
# #VOP    = lg_PTS / (lg_FGA - lg_ORB + lg_TOV + 0.44 * lg_FTA)
# #DRB%   = (lg_TRB - lg_ORB) / lg_TRB
# uPER_player = {}
# team_uPER = []
# for key in player_perf:
#     value = player_perf[key]
#     value = np.array(value) + 1.1
#     value = value.tolist()
#     factor = (2/3) - (0.5 * log(value[2])/log(value[3]))/ 2 * (log(value[3])/log(value[4]))
#     VOP = log(value[-1])/(log(value[6]) - log(value[-5]) + log(value[5]) + 0.44 * log(value[7]))
#     DRB = (log(value[-6]) - log(value[-5])) / log(value[-6])
#     
#     #Here we also need to use team performance for calculating PER
#     team_per = team_perf[player_team[key]]
#     team_ast = team_per[16]
#     team_fg = team_per[1]
#     
#     uPER = (1 / value[0]) *(value[1] + (2/3) * value[2] + (2 - factor * (team_ast / team_fg)) * value[3]
#     + (value[4] *0.5 * (1 + (1 - (team_ast/ team_fg)) + (2/3) * (team_ast/ team_fg)))
#     - VOP * value[5]
#     - VOP * DRB * (value[6] - value[3])
#     - VOP * 0.44 * (0.44 + (0.56 * DRB)) * (value[7] - value[4])
#     + VOP * (1 - DRB) * (value[-6] - value[-5])
#     + VOP * DRB * value[-5]
#     + VOP * value[-4]
#     + VOP * DRB * value[-3]
#     - value[-2] * ((log(value[4])/ log(value[-2])) - 0.44 * (log(value[7]) / log(value[-2])) * VOP))
#     team_uPER.append([player_team[key],uPER])
# 
# uPER_rank = pd.DataFrame(team_uPER)
# uPER_rank[['name','per']] = uPER_rank
# uPER_rank = uPER_rank.sort_values(by = ['per'],ascending = False)
# 
# team_list = list(set(uPER_rank.iloc[0:35,0]))
# ##add the features into our team_performance
# for key, value in team_perf.items():
#     if key in team_list:
#         value.append(1)
#     else:
#         value.append(0)
#         
# ###calculate the substract of two teams
# game_id = list(set((org_data['gameid']))) 
# model_data = []
# for gID in game_id:
#     temp = data.loc[data['gameid'] == gID]
#     result = temp['Win?'].values[0] - temp['Win?'].values[1]
#     home = temp['home'].values[0] - temp['home'].values[1]
#     #for home, -1 means team one is away, 0 means it's a neutral game, 1 means team one is home
#     if (result == -1):
#         result = 0
#     #so 0 represents team one loses, 1 represents team one wins.
#     team1_perf = np.asarray(team_perf[temp['Team'].values[0]][1:])
#     team2_perf = np.asarray(team_perf[temp['Team'].values[1]][1:])
#     team_diff = team1_perf - team2_perf
#     team_diff = np.append(team_diff,home)
#     team_diff = np.append(team_diff,result)
#     model_data.append(team_diff)
# 
# 
# features.remove('Win?')
# features.remove('home')
# features.append('Win_diff')
# features.append('F4')
# features.append('C10')
# features.append('Top_Player')
# features.append('Home')
# features.append('result')
# 
# data_ready = pd.DataFrame(data = model_data, columns = features)
# 
# data_ready.to_csv('data_final.csv')
# 
# data_zero = data_ready[data_ready['Home'] == 0]
# =============================================================================
