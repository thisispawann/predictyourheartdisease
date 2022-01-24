import pandas as pd
import numpy as np
import seaborn as sns
import sklearn
import matplotlib.pyplot as plt
import joblib

# Load and store the data into a variable
df = pd.read_csv("predictor\\heartdata.csv") 


# Splitting the data for training and testing, X is features and Y is target variable
# X -- train _X, test_X 80/20
# Y -- train_Y, test_Y

X = df.drop('target', axis=1)
Y = df['target']

# Train -and- Test  -Split
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=1)

# 1 Logistic Regression
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(X_train, Y_train)

y_pred = lr.predict(X_test)
print(y_pred)

from sklearn.metrics import accuracy_score
ac_lr = accuracy_score(Y_test, y_pred)

print(ac_lr*100,'%')

# Confusion matrix
from sklearn.metrics import confusion_matrix, classification_report
 
cm = confusion_matrix(Y_test, y_pred)
conf_matrix = pd.DataFrame(data = cm,
                           columns = ['Predicted:0', 'Predicted:1'],
                           index =['Actual:0', 'Actual:1'])
plt.figure(figsize = (8, 5))
sns.heatmap(conf_matrix, annot = True, fmt = 'd', cmap = "Greens")
plt.show()
 
print('The details for confusion matrix is =')
print (classification_report(Y_test, y_pred))


# 3. [Using ML algorithm], KNN
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()

knn.fit(X_train, Y_train)

Y_pred = knn.predict(X_test)

from sklearn.metrics import accuracy_score
ac_knn = accuracy_score(Y_test, Y_pred)

ac_knn = accuracy_score(Y_test, Y_pred)

print(ac_knn*100,'%')

# 4. [Using ML algorithm], Random Forest 
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()

rf.fit(X_train, Y_train)

Y_pred = rf.predict(X_test)

from sklearn.metrics import accuracy_score
acc_rf = accuracy_score(Y_test, Y_pred)

print(acc_rf*100,'%') 