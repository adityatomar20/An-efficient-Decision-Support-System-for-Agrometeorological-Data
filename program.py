#!/usr/bin/env python3

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

import matplotlib.gridspec as gridspec



df = pd.read_csv("dataset5.csv")

X = df.iloc[:,[1,2]].values

y = df.iloc[:,[0]].values



df1 = pd.read_csv("dataset4.csv")

final = df1[(df1.Crop == "Rice") | (df1.Crop == "SugarCane") | (df1.Crop == "Cotton") | (df1.Crop == "Millet") | (df1.Crop == "Wheat") | (df1.Crop == "Barley")].copy()

final1 = df[(df.Crop == "Rice") | (df.Crop == "SugarCane") | (df.Crop == "Cotton") | (df.Crop == "Millet") | (df.Crop == "Wheat") | (df.Crop == "Barley")].copy()

final2 = pd.concat([final,final1])

final2.to_csv("final_dataset.csv", sep='\t', index = False)



clean1 = final2[final2.Crop == "Rice"]

Q1 = clean1['Rainfall'].quantile(0.25)

Q3 = clean1['Rainfall'].quantile(0.75)

IQR = Q3-Q1

clean1 = clean1[~((clean1['Rainfall'] < (Q1 - 1.5 * IQR)) | (clean1['Rainfall'] > (Q3 + 1.5 * IQR)))]



clean2 = final2[final2.Crop == "SugarCane"]

Q1 = clean2['Rainfall'].quantile(0.25)

Q3 = clean2['Rainfall'].quantile(0.75)

IQR = Q3-Q1

clean2 = clean2[~((clean2['Rainfall'] < (Q1 - 1.5 * IQR)) | (clean2['Rainfall'] > (Q3 + 1.5 * IQR)))]



clean3 = final2[final2.Crop == "Cotton"]

Q1 = clean3['Rainfall'].quantile(0.25)

Q3 = clean3['Rainfall'].quantile(0.75)

IQR = Q3-Q1

clean3 = clean3[~((clean3['Rainfall'] < (Q1 - 1.5 * IQR)) | (clean3['Rainfall'] > (Q3 + 1.5 * IQR)))]



clean4 = final2[final2.Crop == "Millet"]

Q1 = clean4['Rainfall'].quantile(0.25)

Q3 = clean4['Rainfall'].quantile(0.75)

IQR = Q3-Q1

clean4 = clean4[~((clean4['Rainfall'] < (Q1 - 1.5 * IQR)) | (clean4['Rainfall'] > (Q3 + 1.5 * IQR)))]



clean5 = final2[final2.Crop == "Wheat"]

Q1 = clean5['Rainfall'].quantile(0.25)

Q3 = clean5['Rainfall'].quantile(0.75)

IQR = Q3-Q1

clean5 = clean5[~((clean5['Rainfall'] < (Q1 - 1.5 * IQR)) | (clean5['Rainfall'] > (Q3 + 1.5 * IQR)))]



clean6 = final2[final2.Crop == "Barley"]

Q1 = clean6['Rainfall'].quantile(0.25)

Q3 = clean6['Rainfall'].quantile(0.75)

IQR = Q3-Q1

clean6 = clean6[~((clean6['Rainfall'] < (Q1 - 1.5 * IQR)) | (clean6['Rainfall'] > (Q3 + 1.5 * IQR)))]





Q1 = clean1['Temperature'].quantile(0.25)

Q3 = clean1['Temperature'].quantile(0.75)

IQR = Q3-Q1

clean1 = clean1[~((clean1['Temperature'] < (Q1 - 1.5 * IQR)) | (clean1['Temperature'] > (Q3 + 1.5 * IQR)))]



Q1 = clean2['Temperature'].quantile(0.25)

Q3 = clean2['Temperature'].quantile(0.75)

IQR = Q3-Q1

clean2 = clean2[~((clean2['Temperature'] < (Q1 - 1.5 * IQR)) | (clean2['Temperature'] > (Q3 + 1.5 * IQR)))]



Q1 = clean3['Temperature'].quantile(0.25)

Q3 = clean3['Temperature'].quantile(0.75)

IQR = Q3-Q1

clean3 = clean3[~((clean3['Temperature'] < (Q1 - 1.5 * IQR)) | (clean3['Temperature'] > (Q3 + 1.5 * IQR)))]



Q1 = clean4['Temperature'].quantile(0.25)

Q3 = clean4['Temperature'].quantile(0.75)

IQR = Q3-Q1

clean4 = clean4[~((clean4['Temperature'] < (Q1 - 1.5 * IQR)) | (clean4['Temperature'] > (Q3 + 1.5 * IQR)))]



Q1 = clean5['Temperature'].quantile(0.25)

Q3 = clean5['Temperature'].quantile(0.75)

IQR = Q3-Q1

clean5 = clean5[~((clean5['Temperature'] < (Q1 - 1.5 * IQR)) | (clean5['Temperature'] > (Q3 + 1.5 * IQR)))]



Q1 = clean6['Temperature'].quantile(0.25)

Q3 = clean6['Temperature'].quantile(0.75)

IQR = Q3-Q1

clean6 = clean6[~((clean6['Temperature'] < (Q1 - 1.5 * IQR)) | (clean6['Temperature'] > (Q3 + 1.5 * IQR)))]



Q1 = clean1['Humidity'].quantile(0.25)

Q3 = clean1['Humidity'].quantile(0.75)

IQR = Q3-Q1

clean1 = clean1[~((clean1['Humidity'] < (Q1 - 1.5 * IQR)) | (clean1['Humidity'] > (Q3 + 1.5 * IQR)))]



Q1 = clean2['Humidity'].quantile(0.25)

Q3 = clean2['Humidity'].quantile(0.75)

IQR = Q3-Q1

clean2 = clean2[~((clean2['Humidity'] < (Q1 - 1.5 * IQR)) | (clean2['Humidity'] > (Q3 + 1.5 * IQR)))]



Q1 = clean3['Humidity'].quantile(0.25)

Q3 = clean3['Humidity'].quantile(0.75)

IQR = Q3-Q1

clean3 = clean3[~((clean3['Humidity'] < (Q1 - 1.5 * IQR)) | (clean3['Humidity'] > (Q3 + 1.5 * IQR)))]



Q1 = clean4['Humidity'].quantile(0.25)

Q3 = clean4['Humidity'].quantile(0.75)

IQR = Q3-Q1

clean4 = clean4[~((clean4['Humidity'] < (Q1 - 1.5 * IQR)) | (clean4['Humidity'] > (Q3 + 1.5 * IQR)))]



Q1 = clean5['Humidity'].quantile(0.25)

Q3 = clean5['Humidity'].quantile(0.75)

IQR = Q3-Q1

clean5 = clean5[~((clean5['Humidity'] < (Q1 - 1.5 * IQR)) | (clean5['Humidity'] > (Q3 + 1.5 * IQR)))]



Q1 = clean6['Humidity'].quantile(0.25)

Q3 = clean6['Humidity'].quantile(0.75)

IQR = Q3-Q1

clean6 = clean6[~((clean6['Humidity'] < (Q1 - 1.5 * IQR)) | (clean6['Humidity'] > (Q3 + 1.5 * IQR)))]



finaldf = pd.concat([clean1,clean2,clean3,clean4,clean5,clean6])


res = pd.get_dummies(finaldf['Crop'])

#print (res)


testdf = pd.concat([finaldf,res],sort=False)

from sklearn.preprocessing import LabelEncoder
finaldf.apply(LabelEncoder().fit_transform)
res["Rainfall"]=finaldf['Rainfall']
res['Humidity']=finaldf['Humidity']
res["Temperature"]=finaldf['Temperature']
#print (res)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
X=res.iloc[:,6:]
Y=res.iloc[:,:-3]
x_test = []
X_train,X_test,Y_train,Y_test=train_test_split(X,Y, test_size=0.4, random_state=42)
x_train = np.array(X_train).reshape(-1,3)
regressor=RandomForestClassifier(n_estimators = 100, random_state = 42).fit(x_train,Y_train)
x_test = np.array(X_test)
#x1_test = np.array(x_test).reshape(-1,1)
answer=regressor.predict(x_test)
ytestrfc = np.array(Y_test).tolist()
rfcpred = answer.tolist()
testcount=0.0
for i in range(len(rfcpred)):
    if rfcpred[i] != ytestrfc[i]:
        testcount +=1.0
print("Rfc acc = ", 100-((testcount/len(rfcpred))*100))

'''
final_val=0
for i in range(len(answer)):
    final_val+=abs(answer[i]-x_test[i])/answer[i]
print ((1 - final_val/len(answer))*100,"% accuracy")
'''
'''
dot_data = StringIO()

export_graphviz(regressor, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
Image(graph.create_png())
'''
from sklearn.neighbors import KNeighborsClassifier
new_reg=KNeighborsClassifier(n_neighbors=220, weights='uniform',algorithm='auto',leaf_size=30,p=2,metric='minkowski',metric_params=None, n_jobs=1)
new_reg.fit(x_train,Y_train)
predd = new_reg.predict(x_test.reshape(-1,3))
col_list=["Barley","Cotton","Millet","Rice","SugarCane","Wheat"]

dtreg=DecisionTreeClassifier(max_depth=10).fit(x_train,Y_train)
preddddddd = dtreg.predict(x_test.reshape(-1,3))
ytestdec = np.array(Y_test).tolist()
decpred = preddddddd.tolist()
testcount=0.0
for i in range(len(decpred)):
    if decpred[i] != ytestdec[i]:
        testcount +=1.0
print("Dec acc = ", 100-((testcount/len(decpred))*100))

from sklearn.externals.six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus
'''
dot_data = StringIO()

export_graphviz(dtreg, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
Image(graph.create_png())
'''


new_reg1=KNeighborsClassifier(n_neighbors=220, weights='uniform',algorithm='auto',leaf_size=30,p=1,metric='minkowski',metric_params=None, n_jobs=1)
new_reg1.fit(x_train,Y_train)
preddd=new_reg1.predict(x_test.reshape(-1,3))
print (preddd)
testcount = 0.0
manpred = preddd.tolist()
ytestm = np.array(Y_test).tolist()

eucpred = predd.tolist()
ytesteuc = np.array(Y_test).tolist()

for i in range(len(manpred)):
    if manpred[i] != ytestm[i]:
        testcount +=1.0
print("man acc = ", 100-((testcount/len(manpred))*100))

testcount=0.0
for i in range(len(eucpred)):
    if eucpred[i] != ytesteuc[i]:
        testcount +=1.0
print("Euc acc = ", 100-((testcount/len(eucpred))*100))  

new_reg2=KNeighborsClassifier(n_neighbors=220, weights='uniform',algorithm='auto',leaf_size=30,p=5,metric='minkowski',metric_params=None, n_jobs=1)
new_reg2.fit(x_train,Y_train)
preddddi=new_reg2.predict(x_test.reshape(-1,3))
minkpred = preddddi.tolist()
ytestmink = np.array(Y_test).tolist()
testcount = 0.0
for i in range(len(minkpred)):
    if minkpred[i] != ytestmink[i]:
        testcount +=1.0
print("mink acc = ", 100-((testcount/len(minkpred))*100))
