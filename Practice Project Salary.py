#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[42]:


pd.read_csv('https://raw.githubusercontent.com/MaheshAgashimani/Internship-Mahesh1416/master/Salaries.csv')


# In[43]:


df=pd.read_csv("https://raw.githubusercontent.com/MaheshAgashimani/Internship-Mahesh1416/master/Salaries.csv")


# In[44]:


df


# In[5]:


df.head()


# In[6]:


df.tail(2)


# In[45]:


df.columns


# In[46]:


df.isnull()


# In[47]:


df.isnull().sum()


# In[48]:


df.columns


# In[49]:


#EDA Part
import seaborn as sns


# In[50]:


sns.scatterplot()


# In[13]:


sns.scatterplot(x="rank",y="salary",data=df)


# In[14]:


sns.scatterplot(x="discipline",y="salary",data=df)


# In[16]:


sns.scatterplot(x="yrs.since.phd",y="salary",data=df)


# In[17]:


sns.scatterplot(x="yrs.service",y="salary",data=df)


# In[18]:


sns.scatterplot(x="sex",y="salary",data=df)


# In[19]:


import matplotlib.pyplot as plt
sns.pairplot(df)
plt.savefig('pairplot.png')
plt.show()


# In[51]:


df.corr()


# In[52]:


df.corr()['salary'].sort_values()


# In[22]:


# Correlation using Heatmap
import matplotlib.pyplot as plt
plt.figure(figsize=(15,7))
sns.heatmap(df.corr(),annot=True,linewidth=0.5,linecolor='Black',fmt='.2f')


# In[53]:


#Descriptive Statistics
#Desribing Datasets (For Numerical Values)
df.describe()


# In[24]:


plt.figure(figsize=(15,12))
sns.heatmap(round(df.describe()[1:].transpose(),2),linewidth=2,annot=True,fmt="f")
plt.xticks(fontsize=18)
plt.yticks(fontsize=12)
plt.title("Variables Summary")
plt.savefig('heatamap.png')
plt.show()


# In[25]:


df.info()


# In[54]:


#Skewness
df.skew()


# In[29]:


# Skewness between -065 to 0.65
#Clumns are ("Pregnancies,BloodPressure,Insulin,DiabetesPedigreeFunction,Age")


# In[55]:


df.corr()['salary']


# In[56]:


delete=pd.DataFrame([["1.000000","salary","No","Alot"]],columns=["Correlation with Target","Column Name","Normalised","Outliers"])
delete


# In[59]:


x=df.drop(["salary"],axis=1)
y=df['salary']


# In[60]:


x.shape , y.shape


# In[78]:


#Splitting the DataFrame

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
from sklearn.metrics import accuracy_score


# In[66]:


d = df.drop(['rank'],axis=1)


# In[67]:


d


# In[69]:


df


# In[87]:


df = df.drop(['rank'],axis=1)


# In[96]:


df = df.drop(['discipline'],axis=1)
df


# In[ ]:





# In[97]:


from scipy.stats import zscore


# In[98]:


z = np.abs(zscore(df))


# In[99]:


z.shape


# In[100]:


# threshold = (-3,3)
#if applied np.abs
threshold = 3

#index number
print(np.where(z>3))


# In[101]:


len(np.where(z>3)[0])


# In[102]:


df_new=df[(z<3).all(axis=1)]


# In[103]:


print("Old Dataframe",df.shape)
print("New Dataframe",df_new.shape)
print("Total Dropped Rows",df.shape[0] - df_new.shape[0])


# In[105]:


# Percentage Data Loss
loss_percent = (397-393)/397*100
print(loss_percent,'%')


# In[106]:


# Model without outliers df

df_new


# In[107]:


#independant Column
x=df_new.iloc[:,:-1]


# In[108]:


#target
y=df_new.iloc[:,-1]


# In[109]:


# Transforming data to remove skewness
from sklearn.preprocessing import power_transform
x=power_transform(x,method='yeo-johnson')
x


# In[113]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
from sklearn.metrics import accuracy_score


# In[114]:


for i in range(0,1000):
    x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=i,test_size=0.20)
    lr.fit(x_train,y_train)
    pred_train = lr.predict(x_train)
    pred_test = lr.predict(x_test)
    if round(accuracy_score(y_train,pred_train)*100,1) == round(accuracy_score(y_test,pred_test)*100,1):
        print("At Random State",i,"The model performs very well")
        print("At Random State:-",i)
        print("Training accuracy score is:-",round(accuracy_score(y_train,pred_train)*100,1))
        print("Testing accuracy score is:-",round(accuracy_score(y_test,pred_test)*100,1),'\n\n')


# In[115]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20,random_state=552)


# In[116]:


from sklearn.metrics import classification_report
print(classification_report(y_test,pred_test))


# In[117]:


#Cross Validation score for logistic regression
pred_lr=lr.predict(x_test)
from sklearn.model_selection import cross_val_score
lss=accuracy_score(y_test,pred_lr)


# In[118]:


for j in range(2,10):
    lsscore = cross_val_score(lr,x,y,cv=j)
    lsc=lsscore.mean()
    print("At CV:-",j)
    print("Cross Validation Score is:-",lsc*100)
    print("accuracy Score is:-",lss*100)
    print("\n")


# In[119]:


lsscore_selected = cross_val_score(lr,x,y,cv=5).mean()
print("The CV Score is:",lsscore_selected,"\n The accuracy score is:",lss)


# In[122]:


lr.score(x_test,y_test)


# In[126]:


from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


rnse = np.sqrt(mean_squared_error(y_test,pred_test))
r2 = r2_score(y_test,pred_test)


# In[127]:


rnse, r2


# In[133]:


# AUC ROC Curve:


# In[134]:


import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
plt.scatter(x=y_test,y=pred_test,color='r')
plt.plot(y_test,pred_test,color='b')
plt.xlabel('Actual Value',fontsize=14)
plt.ylabel('Predicted Value',fontsize=14)
plt.title('Linear Regression',fontsize=18)
plt.show()


# In[135]:


from sklearn.metrics import roc_curve,auc
fpr,tpr,thresholds = roc_curve(pred_test,y_test)
roc_auc = auc(fpr,tpr)

plt.figure()
plt.plot(fpr,tpr,color='darkorange',lw=10,label='ROC Curve (are = %0.2f)'% roc_auc)
plt.plot([0,1],[0,1], color='navy',lw=10,linestyle='--')
plt.xlim([0.0,1.0])
plt.ylim([0.0,1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()


# In[136]:


#Model Saving

import pickle
filename = 'Salary_pk1'
pickle.dump(lr,open(filename,'wb'))


# In[137]:


# Conclusion:

import numpy as np
a=np.array(y_test)
predicted = np.array(lr.predict(x_test))
df_com=pd.DataFrame({"origional":a,"predicted":predicted},index=range(len(a)))
df_com


# In[ ]:




