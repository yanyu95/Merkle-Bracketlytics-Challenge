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

# =============================================================================
# #building model1--logistic regression
# from sklearn.linear_model import LogisticRegression
# classifier = LogisticRegression(random_state = 0)
# classifier.fit(X_train, y_train)
# ##building model2--KNN
# from sklearn.neighbors import KNeighborsClassifier
# classifier = KNeighborsClassifier(n_neighbors = 1, metric = 'minkowski', p = 2)
# classifier.fit(X_train, y_train)
# ##building model3--svc
# from sklearn.svm import SVC
# classifier = SVC(kernel = 'rbf', random_state = 0)
# classifier.fit(X_train, y_train)
# ##building model4--decision tree
# from sklearn.tree import DecisionTreeClassifier
# classifier = DecisionTreeClassifier(criterion = 'entropy',random_state = 0)
# classifier.fit(X_train, y_train)
# ##building model5--decision tree
# from sklearn.ensemble import RandomForestClassifier
# classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
# classifier.fit(X_train, y_train)
# =============================================================================
##building model6--gradient boosting classifier
from sklearn.ensemble import GradientBoostingClassifier
classifier = GradientBoostingClassifier(n_estimators=100, learning_rate=0.2, max_depth=1, random_state=0)
classifier.fit(X_train, y_train)
# =============================================================================
# ##building model7 -- ridge classifier
# from sklearn.linear_model import RidgeClassifier
# classifier = RidgeClassifier(solver="lsqr")
# classifier.fit(X_train, y_train)
# =============================================================================
#for each model we run the following function to select three with highest accuracy
from sklearn.model_selection import cross_val_score
def benchmark2(classifier):  
    print('_' * 80)  
    print("Training: ")  
    print(classifier)
    classifier.fit(X_train, y_train)
    score1 = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10).mean()
    print("trianing accuracy:   %0.3f" % score1)  
    score2 = cross_val_score(estimator = classifier, X = X_test, y = y_test, cv = 10).mean()
    print("test accuracy:   %0.3f" % score2)  
    clf_descr = str(classifier).split('(')[0]  
    return clf_descr, score1, score2
benchmark2(classifier)




















