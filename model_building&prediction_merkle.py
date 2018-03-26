import numpy as np
import pandas as pd 

dataset = pd.read_csv('data_final.csv')
dataset = dataset.drop('Unnamed: 0', axis = 1)
#balance wins and loses
X_data = []
Y_data = []
for index, row in dataset.iterrows():
    if (index % 2) == 0:
        if (row['result'] == 0):
            X_data.append(row[:-1])
            Y_data.append(0)
        else:
            X_data.append(row[:-1]*-1)
            Y_data.append(0)
    else:
        if (row['result'] == 1):
            X_data.append(row[:-1])
            Y_data.append(1)
        else:
            X_data.append(row[:-1]*-1)
            Y_data.append(1)
#create data frame again
X_data = pd.DataFrame(data = X_data)
Y_data = pd.DataFrame(data = Y_data)
#create column name for y
Y_data.columns = ['result']
#create a list to save all features
all_feature = X_data.columns
#select all features
X_data_select = X_data[all_feature]
#Split data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_data_select, Y_data, test_size = 0.25, random_state = 0)
#feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

####feature selection
from sklearn.ensemble import GradientBoostingClassifier
clf = GradientBoostingClassifier()
clf.fit(X_train, y_train)
ft = clf.feature_importances_
interest = []
for i in range(len(ft)):
    if ft[i] > 0.02:
        interest.append(all_feature[i])

X_data_select = X_data[interest]
#split and scale again
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_data_select, Y_data, test_size = 0.25, random_state = 0)
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

from sklearn.ensemble import GradientBoostingClassifier
classifier = GradientBoostingClassifier(n_estimators=100, learning_rate=0.2, max_depth=1, random_state=0).fit(X_train, y_train)


divi = ['virginia', 'maryland-baltimore-county', 'creighton', 'kansas-state', 'kentucky', 'davidson', 'arizona', 'buffalo', 'miami-fl',
        'loyola-il', 'tennessee', 'wright-state', 'nevada', 'texas', 'cincinnati', 'georgia-state', 'xavier', 'texas-southern',
        'missouri', 'florida-state', 'ohio-state', 'south-dakota-state', 'gonzaga', 'north-carolina-greensboro', 'houston', 
        'san-diego-state', 'michigan', 'montana', 'texas-am', 'providence', 'north-carolina', 'lipscomb',
        'villanova', 'radford', 'virginia-tech', 'alabama', 'west-virginia', 'murray-state', 'wichita-state', 'marshall',
        'florida', 'st-bonaventure', 'texas-tech', 'stephen-f-austin', 'arkansas', 'butler', 'purdue', 'cal-state-fullerton', 'kansas',
        'pennsylvania', 'seton-hall', 'north-carolina-state', 'clemson', 'new-mexico-state', 'auburn', 'college-of-charleston',
        'texas-christian', 'syracuse', 'michigan-state', 'bucknell', 'rhode-island', 'oklahoma', 'duke', 'iona']

team_data = pd.read_csv('team_perf.csv')
team_data = team_data.drop('Unnamed: 0',axis = 1)
team_stat = team_data.drop('Team',axis = 1)

def predict(divi, classifier):
    #read team performance
    num_team = len(divi)
    win_team = []
    for i in range(0, num_team, 2):
        team1 = np.asarray(team_stat.loc[team_data['Team'] == divi[i]])
        team2 = np.asarray(team_stat.loc[team_data['Team'] == divi[i+1]])
        team_diff = team1 - team2
        team_diff = np.append(team_diff,0)
        team_diff = np.reshape(team_diff, (1, 47))
        team_ready = pd.DataFrame(team_diff,columns = all_feature)[interest]
        team_x = sc_X.transform(team_ready)
        result = classifier.predict(team_x)
        if result[0] == 1:
            win_team.append(divi[i])
        else:
            win_team.append(divi[i+1])
    print(win_team)
    if len(win_team) == 1:
        return win_team
    return (predict(win_team, classifier))
    
champ = predict(divi, classifier)