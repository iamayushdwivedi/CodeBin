#IMPORTING OUR PACKAGES FOR THE PROJECT
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC

#COLLECTION OF THE DATA
df = pd.read_csv("train.csv") #TRAINING DATA
df_1 = pd.read_csv("test.csv") #TESTING DATA
df_2 = [df , df_1] #COMBINED DATA OF TESTING AND TRAINING

print(df.columns.values) #THIS WILL GIVE US THE COLUMN NAMES
print(df.head())

df.info()
print("*"*100)
df_1.info()

print("*"*100)
print(df.describe())

#PLOTTING OF GRAPHS
# HIST GRAPH
plt.figure(1)
df.hist()
plt.show()

#BOX PLOT
plt.figure(2)
df.plot(kind = 'box' , subplots = True , layout = (3,3) , sharex = False)
plt.show()

#BAR GRAPH TO SHOW THE PERCENTAGE OF PASSENGERS WHO SURVIVED AND DECEASED

df.Survived.value_counts(normalize = True).plot(kind = 'bar', alpha = 0.7)
plt.title("SURVIVED AND DECEASED")
plt.show()

#SCATTER GRAPH THAT SHOWS THE RELATION BETWEEN SURVIVAL AND AGE
plt.scatter(df.Survived, df.Age, alpha = 0.1)
plt.title("Relation Between Survival and Age")
plt.show()

#A BARGRAPH TO SHOW THAT PASSENGERS BELONG TO WHICH CLASS
df.Pclass.value_counts(normalize = True).plot(kind = 'bar', alpha = 0.7)
plt.title("Class Distribution")
plt.show()

#KERNEL DENSITY GRAPH BETWEEN CLASS AND AGE
for i in [1, 2, 3]:
    df.Age[df.Pclass == i].plot(kind = 'kde', alpha = 0.8)
plt.title("Class V/S Age")
plt.legend("123")
plt.show()

#PLACE OF EMBARKATION
df.Embarked.value_counts(normalize = True).plot(kind = 'bar', alpha = 0.7)
plt.title("PLACE OF EMBARKATION")
plt.show()

#CORRELATION WITH GENDER
df.Survived[df.Sex == 'male'].value_counts(normalize = True).plot(kind = 'bar', alpha = 0.5 , color = 'r')
plt.title("MALE SURVIVED")
plt.show()

df.Survived[df.Sex == 'female'].value_counts(normalize = True).plot(kind = 'bar' , alpha = 0.5 , color = 'g')
plt.title("FEMALE SURVIVED")
plt.show()

df.Sex[df.Survived == 1].value_counts(normalize = True).plot(kind = 'bar', alpha = 0.5, color = ['r', 'g'])
plt.title("SURVIVAL ON THE BASIS OF GENDER")
plt.show()
'''From here we come to know that among all the survivors 70% were females and 30% were males'''

#A KERNEL DENSITY GRAPH THAT SHOWS RELATION BETWEEN CLASS AND SURVIVED
for i in [1, 2, 3]:
    df.Survived[df.Pclass == i].plot(kind = 'kde', alpha = 0.8)
plt.title("CLASS V/S SURVIVED")
plt.legend(("1st", "2nd", "3rd"))
plt.show()
'''The above graph shows 3rd class passengers have high mortality rate compared to 1st class passengers'''

#A GRAPH TO SHOW SURVIVAL RATE OF RICH MALE, POOR MALE, RICH FEMALE, POOR FEMALE RESPECTIVELY
plt.subplot2grid((4, 4), (0, 0))
df.Survived[(df.Sex == 'male') & (df.Pclass == 1)].value_counts(normalize = True).plot(kind = 'bar', alpha = 0.5, color = 'r')
plt.title("RICH MALE SURVIVED")


plt.subplot2grid((4, 4), (0, 1))
df.Survived[(df.Sex == 'male') & (df.Pclass == 3)].value_counts(normalize = True).plot(kind = 'bar', alpha = 0.5, color = 'r')
plt.title("POOR MALE SURVIVED")


plt.subplot2grid((4, 4), (0, 2))
df.Survived[(df.Sex == 'female') & (df.Pclass == 1)].value_counts(normalize = True).plot(kind = 'bar', alpha = 0.5, color = 'g')
plt.title("RICH FEMALE SURVIVED")


plt.subplot2grid((4, 4), (0, 3))
df.Survived[(df.Sex == 'female') & (df.Pclass == 3)].value_counts(normalize = True).plot(kind = 'bar', alpha = 0.5, color = 'g')
plt.title("POOR FEMALE SURVIVED")
plt.show()
'''From the above graphs we will see that 40% of rich men survived while 60% died
10% of poor men survived where as 90% of them died.. Less than 1% of rich women died
whereas 50% of poor women survived and other 50% died'''

#CLEANING OF DATA

def clean_data(data):
    data["Fare"] = data["Fare"].fillna(data["Fare"].dropna().median())
    data["Age"] = data["Age"].fillna(data["Age"].dropna().median())
    data.loc[data["Sex"] == 'male', "Sex"] = 0
    data.loc[data["Sex"] == 'female', "Sex"] = 1
    data["Embarked"] = data["Embarked"].fillna("S")
    data.loc[data["Embarked"] == "S", "Embarked"] = 0
    data.loc[data["Embarked"] == "C", "Embarked"] = 1
    data.loc[data["Embarked"] == "Q", "Embarked"] = 2
'''Here we have used a function clean_data which finds data set where Fare and Age have 
no value and fills them with median values of those columns respectively. Also for 
convenience, it marks male passengers as 0 and female passengers as 1. Also, in Embaked 
column the blank cells are filled with S. Also we have marked S as 0, C as 1, Q as 2.'''

# Linear Regression
from sklearn import linear_model

train = pd.read_csv("train.csv")
clean_data(train)

target = train["Survived"].values
features = train[["Pclass", "Age", "Fare", "Embarked", "Sex", "SibSp", "Parch"]].values

classifier = linear_model.LogisticRegression()
classifier_ = classifier.fit(features, target)

lr_score = print(classifier_.score(features , target)*100, 2)

#THE ABOVE CODE GIVES US A SCORE of 0.799102 i.e 79.91% of accuracy in prediction
# Polynomial Featuring
from sklearn import linear_model, preprocessing

poly = preprocessing.PolynomialFeatures(degree = 2)
poly_features = poly.fit_transform(features)

classifier_ = classifier.fit(poly_features, target)

poly_score = print(classifier_.score(poly_features, target)*100, 2)
'''The above code gives us a score of 0.82603815937 or 82.60% of accuracy in prediction.'''
# Decision Tree
from sklearn import tree

train = pd.read_csv("train.csv")
clean_data(train)

target = train["Survived"].values

features = train[["Pclass", "Age", "Fare", "Embarked", "Sex", "SibSp", "Parch"]].values

decision_tree = tree.DecisionTreeClassifier(random_state= 1)
decision_tree = decision_tree.fit(features, target)

tree_score = print(decision_tree.score(features , target)*100 , 2)
'''The above code gives us a accuracy of 97.97%. So we can see that decision tree is 
producing more accurate results as compared to regression in this case'''
# Support Vector Machines
svc = SVC()

train = pd.read_csv("train.csv")
clean_data(train)

target = train["Survived"].values
features = train[["Pclass", "Age", "Fare", "Embarked", "Sex", "SibSp", "Parch"]].values
svc.fit(features, target)
svc_score = print(svc.score(features, target)*100, 2)
'''The above code gives us a accuracy of 89.22% as prediction'''

# KNearest Neighbours
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors= 3)
target = train["Survived"].values
features = train[["Pclass", "Age", "Fare", "Embarked", "Sex", "SibSp", "Parch"]].values
knn.fit(features, target)
knn_score = print(knn.score(features, target)*100, 2)
'''The above code gives us a accuracy score of 83.95% as prediction'''

# Gaussian Naive Bayes
from sklearn.naive_bayes import GaussianNB

gaussian = GaussianNB()
target = train["Survived"].values
features = train[["Pclass", "Age", "Fare", "Embarked", "Sex", "SibSp", "Parch"]].values
gaussian.fit(features, target)
gaussian_score = print(gaussian.score(features, target)*100, 2)
'''The above code gives us a accuracy score of 79.23% as prediction'''

models = pd.DataFrame({'Model': ['Linear Regression', 'Polynomial Featuring', 'Decision Tree', 'SVC', 'KNN', 'GaussianNB'],
                       'Score': [lr_score, poly_score, tree_score, svc_score, knn_score, gaussian_score]})
print(models.sort_values(by = 'Score', ascending= False))

# END OF THE PROGRAM
# THANKYOU FOR READING MY PROGRAM