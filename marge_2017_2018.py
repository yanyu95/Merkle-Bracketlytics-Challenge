import numpy as np 
import pandas as pd 

data_2017 = pd.read_csv('2017dataHasHome.csv')
dataset_2017 = data_2017.drop(['Unnamed: 0','Unnamed: 0.1','gameid'],axis = 1)

#Normalize those game which have extra time to regualr time 200
for index, row in dataset_2017.iterrows():
    mp = row['MP']
    if mp > 200:
        dataset_2017.iloc[index, 2:-2] = dataset_2017.iloc[index, 2:-2] * 200/mp
#Now we can get rid of MP
dataset_2017 = dataset_2017.drop(['MP'],axis = 1)        
#find all the  team
team_names =list(set((dataset_2017['Team'])))


data_2018 = pd.read_csv('2018dataHasHome.csv')
#change win to 1, lose to 0 to make it consistent with 2017 data
for index, row in data_2018.iterrows():
    if row['PTS'] > row['Opp PTS']:
        data_2018.loc[index, "Win?"] = 1
    else:
        data_2018.loc[index, "Win?"] = 0
        
dataset_2018 = data_2018.drop(['Unnamed: 0','Unnamed: 0.1','gameid'],axis = 1)

#Normalize those game which have extra time to regualr time 200
for index, row in dataset_2018.iterrows():
    mp = row['MP']
    if mp > 200:
        dataset_2018.iloc[index, 2:-2] = dataset_2018.iloc[index, 2:-2] * 200/mp
#Now we can get rid of MP
dataset_2018 = dataset_2018.drop(['MP'],axis = 1)        
#find all the  team
team_names_2017 =list(set((dataset_2017['Team'])))   
team_names_2018 =list(set((dataset_2018['Team'])))
for i in team_names_2017:
    if i not in team_names_2018:
        team_names_2018.append(i)
        
#calculate team dictionary
team_perf = {}
for team in team_names_2018:
    temp_2017 = dataset_2017.loc[dataset_2017['Team'] == team]
    temp_2018 = dataset_2018.loc[dataset_2018['Team'] == team]
    if (len(temp_2017) > 0) & (len(temp_2018) > 0):
        team_index = dataset_2017.index[dataset_2017['Team'] == team]
        need_average_2017 = temp_2017.drop(['Win?','Team','home'],axis = 1)
        need_average_2018 = temp_2018.drop(['Win?','Team','home'],axis = 1)
        mean_2017 = np.mean(need_average_2017)
        mean_2018 = np.mean(need_average_2018)
        # we only sum up the win games in regular season
        team_regular_2017 = []
        for i in team_index:
            if i < 11680:
                team_regular_2017.append(i)
        sum_win_2017 = dataset_2017.iloc[team_regular_2017]['Win?'].sum()
        #while the two first four games that happened before the index of 11680, so we have to minus one to the winner 
        if team in ['mount-st-marys','kansas-state']:
            sum_win_2017 -=1
        mean = (mean_2017 + mean_2018)/2
        sum_win_2018 = temp_2018['Win?'].sum()
        sum_win = sum_win_2017 + sum_win_2018
        mean = np.array(mean)
        mean = np.append(mean, [sum_win])
        a = mean.tolist()
        a.insert(0,team)
        team_perf[team] = a
    elif (len(temp_2017) > 0) & (len(temp_2018) == 0) :
        temp = dataset_2017.loc[dataset_2017['Team'] == team]
        team_index = dataset_2017.index[dataset_2017['Team'] == team]
        need_average = temp.drop(['Win?','Team','home'],axis = 1)
        mean = np.mean(need_average)
        # we only sum up the win games in regular season
        team_regular = []
        for i in team_index:
            if i < 11680:
                team_regular.append(i)
        sum_win = dataset_2017.iloc[team_regular]['Win?'].sum()
        #while the two first four games that happened before the index of 11680, so we have to minus one to the winner 
        if team in ['mount-st-marys','kansas-state']:
            sum_win -=1
        mean = np.array(mean)
        mean = np.append(mean, [sum_win])
        a = mean.tolist()
        a.insert(0,team)
        team_perf[team] = a
    else:
        temp = dataset_2018.loc[dataset_2018['Team'] == team]
        need_average = temp.drop(['Win?','Team','home'],axis = 1)
        mean = np.mean(need_average)
        sum_win = temp['Win?'].sum()
        mean = np.array(mean)
        mean = np.append(mean, [sum_win])
        a = mean.tolist()
        a.insert(0,team)
        team_perf[team] = a
        

#add new variable
#Final four from 2007 to 2017
F4 = pd.read_csv('TOP4(2007-2017).csv')
dataset_F4 = F4.drop(['Rank','Year'],axis = 1)
dataset_F4
F4_teams = list(set(dataset_F4['Team'])) 
F4_teams

for key, value in team_perf.items():
    if key in F4_teams:
        value.append(1)
    else:
        value.append(0)
#
conference = pd.read_csv('Competitive Conference.csv')
new_conference=conference[['conference','Team name']]
new_conference=list(set(new_conference['Team name']))

for key,value in team_perf.items():
    if key in new_conference:
        value.append(1)
    else:
        value.append(0)
        

####deal with player info
from math import log

player_data = pd.read_csv('2018PlayerStats Final.csv')

dataset = player_data.drop(['Unnamed: 0','gameid'],axis = 1)
dataset2 = player_data[['player','MP','3P','AST','FG','FT','TOV','FGA','FTA','TRB','ORB','STL','BLK','PF','PTS']]
player_names = list(set(dataset2['player']))
player_perf = {}

player_team = {}


for player in player_names:
    temp = dataset2.loc[dataset2['player'] == player]
    need_average = temp.drop(['player'],axis = 1)
    mean = np.mean(need_average)
    mean = mean.tolist()
    player_perf[player] = mean
    
    team_name = dataset.loc[dataset['player'] == player].iloc[0][-1]
    player_team[player] = team_name
    
#factor = (2 / 3) - (0.5 * (lg_AST / lg_FG)) / (2 * (lg_FG / lg_FT))
#VOP    = lg_PTS / (lg_FGA - lg_ORB + lg_TOV + 0.44 * lg_FTA)
#DRB%   = (lg_TRB - lg_ORB) / lg_TRB
uPER_player = {}
team_uPER = []
for key in player_perf:
    value = player_perf[key]
    value = np.array(value) + 1.1
    value = value.tolist()
    factor = (2/3) - (0.5 * log(value[2])/log(value[3]))/ 2 * (log(value[3])/log(value[4]))
    VOP = log(value[-1])/(log(value[6]) - log(value[-5]) + log(value[5]) + 0.44 * log(value[7]))
    DRB = (log(value[-6]) - log(value[-5])) / log(value[-6])
    
    #Here we also need to use team performance for calculating PER
    team_per = team_perf[player_team[key]]
    team_ast = team_per[16]
    team_fg = team_per[1]
    
    uPER = (1 / value[0]) *(value[1] + (2/3) * value[2] + (2 - factor * (team_ast / team_fg)) * value[3]
    + (value[4] *0.5 * (1 + (1 - (team_ast/ team_fg)) + (2/3) * (team_ast/ team_fg)))
    - VOP * value[5]
    - VOP * DRB * (value[6] - value[3])
    - VOP * 0.44 * (0.44 + (0.56 * DRB)) * (value[7] - value[4])
    + VOP * (1 - DRB) * (value[-6] - value[-5])
    + VOP * DRB * value[-5]
    + VOP * value[-4]
    + VOP * DRB * value[-3]
    - value[-2] * ((log(value[4])/ log(value[-2])) - 0.44 * (log(value[7]) / log(value[-2])) * VOP))
    team_uPER.append([player_team[key],uPER])

uPER_rank = pd.DataFrame(team_uPER)
uPER_rank[['name','per']] = uPER_rank
uPER_rank = uPER_rank.sort_values(by = ['per'],ascending = False)

team_list = list(set(uPER_rank.iloc[0:50,0]))
##add the features into our team_performance
for key, value in team_perf.items():
    if key in team_list:
        value.append(1)
    else:
        value.append(0)



##here we should save the team performance because we need to extract team info when we compare their difference
team_features = list(data_2018.columns.values)[2:]
team_features.remove('MP')
team_features.remove('Win?')
team_features.remove('home')
team_features.remove('gameid')
team_features.append('WinDiff')
team_features.append('F4')
team_features.append('C10')
team_features.append('Top_Player')

df_team_perf = pd.DataFrame.from_dict(team_perf, orient='index')
df_team_perf.columns = team_features
#save team performance to be prepared for model building
df_team_perf.to_csv('team_perf.csv')
                
        
###calculate the substract of two teams
game_id_2017 = list(set((data_2017['gameid'])))
game_id_2018 = list(set((data_2018['gameid'])))

model_data = []
for gID in game_id_2017:
    temp = data_2017.loc[data_2017['gameid'] == gID]
    result = temp['Win?'].values[0] - temp['Win?'].values[1]
    home = temp['home'].values[0] - temp['home'].values[1]
    #for home, -1 means team one is away, 0 means it's a neutral game, 1 means team one is home
    if (result == -1):
        result = 0
    #so 0 represents team one loses, 1 represents team one wins.
    team1_perf = np.asarray(team_perf[temp['Team'].values[0]][1:])
    team2_perf = np.asarray(team_perf[temp['Team'].values[1]][1:])
    team_diff = team1_perf - team2_perf
    team_diff = np.append(team_diff,home)
    team_diff = np.append(team_diff,result)
    model_data.append(team_diff)
    
for gID in game_id_2018:
    temp = data_2018.loc[data_2018['gameid'] == gID]
    result = temp['Win?'].values[0] - temp['Win?'].values[1]
    home = temp['home'].values[0] - temp['home'].values[1]
    #for home, -1 means team one is away, 0 means it's a neutral game, 1 means team one is home
    if (result == -1):
        result = 0
    #so 0 represents team one loses, 1 represents team one wins.
    team1_perf = np.asarray(team_perf[temp['Team'].values[0]][1:])
    team2_perf = np.asarray(team_perf[temp['Team'].values[1]][1:])
    team_diff = team1_perf - team2_perf
    team_diff = np.append(team_diff,home)
    team_diff = np.append(team_diff,result)
    model_data.append(team_diff)


team_features.remove('Team')
team_features.append('Home')
team_features.append('result')

data_ready = pd.DataFrame(data = model_data, columns = team_features)
#save the data for model building
data_ready.to_csv('data_final.csv')









