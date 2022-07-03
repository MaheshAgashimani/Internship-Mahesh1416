#!/usr/bin/env python
# coding: utf-8

# In[59]:


import pandas as pd
import numpy as np


# In[60]:


pd.read_csv('https://raw.githubusercontent.com/MaheshAgashimani/Internship-Mahesh1416/master/happiness_score_dataset.csv')


# In[61]:


df=pd.read_csv("https://raw.githubusercontent.com/MaheshAgashimani/Internship-Mahesh1416/master/happiness_score_dataset.csv")


# In[62]:


df


# In[63]:


df.head()


# In[64]:


df.columns


# In[65]:


df.isnull().sum()


# In[66]:


df.columns


# In[67]:


#EDA Part
import seaborn as sns


# In[68]:


sns.scatterplot()


# In[14]:


sns.scatterplot(x="Country",y="Dystopia Residual",data=df)


# In[15]:


sns.scatterplot(x="Region",y="Dystopia Residual",data=df)


# In[16]:


sns.scatterplot(x="Happiness Rank",y="Dystopia Residual",data=df)


# In[17]:


sns.scatterplot(x="Happiness Score",y="Dystopia Residual",data=df)


# In[18]:


sns.scatterplot(x="Standard Error",y="Dystopia Residual",data=df)


# In[19]:


sns.scatterplot(x="Economy (GDP per Capita)",y="Dystopia Residual",data=df)


# In[20]:


sns.scatterplot(x="Family",y="Dystopia Residual",data=df)


# In[21]:


sns.scatterplot(x="Health (Life Expectancy)",y="Dystopia Residual",data=df)


# In[22]:


sns.scatterplot(x="Freedom",y="Dystopia Residual",data=df)


# In[23]:


sns.scatterplot(x="Trust (Government Corruption)",y="Dystopia Residual",data=df)


# In[24]:


sns.scatterplot(x="Generosity",y="Dystopia Residual",data=df)


# In[25]:


import matplotlib.pyplot as plt
sns.pairplot(df)
plt.savefig('pairplot.png')
plt.show()


# In[69]:


# Correlation

df.corr()


# In[70]:


df.corr()['Dystopia Residual'].sort_values()


# In[28]:


# Correlation using HeatMap


# In[71]:


import matplotlib.pyplot as plt
plt.figure(figsize=(15,7))
sns.heatmap(df.corr(),annot=True,linewidth=0.5,linecolor='Black',fmt='.2f')


# In[72]:


#Descriptive Statistics
#Desribing Datasets (For Numerical Values)
df.describe()


# In[73]:


plt.figure(figsize=(15,12))
sns.heatmap(round(df.describe()[1:].transpose(),2),linewidth=2,annot=True,fmt="f")
plt.xticks(fontsize=18)
plt.yticks(fontsize=12)
plt.title("Variables Summary")
plt.savefig('heatamap.png')
plt.show()


# In[74]:


df.info()


# In[75]:


#Outliers Checking

import warnings
warnings.filterwarnings('ignore')


# In[76]:


collist = df.columns.values
ncol = 30
nrows = 14
plt.figure(figsize=(ncol,3*ncol))
for i in range(0,len(collist)):
    plt.subplot(nrows,ncol,i+1)
    sns.boxplot(data=df[collist[i]],color='green',orient='v')
    plt.tight_layout()


# In[77]:


#Skewness
df.skew()


# In[36]:


# Skewness between -065 to 0.65
#Clumns are ("Pregnancies,BloodPressure,Insulin,DiabetesPedigreeFunction,Age")


# In[78]:


# Normal Distribution Curve
sns.distplot(df['Happiness Rank'])


# In[79]:


sns.distplot(df['Happiness Score'])


# In[39]:


sns.distplot(df['Standard Error'])


# In[40]:


sns.distplot(df['Economy (GDP per Capita)'])


# In[41]:


sns.distplot(df['Family'])


# In[42]:


sns.distplot(df['Health (Life Expectancy)'])


# In[43]:


sns.distplot(df['Freedom'])


# In[44]:


sns.distplot(df['Trust (Government Corruption)'])


# In[45]:


sns.distplot(df['Generosity'])


# In[46]:


sns.distplot(df['Dystopia Residual'])


# In[80]:


df.corr()['Dystopia Residual']


# In[81]:


delete=pd.DataFrame([["-0.521999","Happiness Rank","No","Alot"],["-0.033105","Trust (Government Corruption)","No","Alot"],["-0.101.301","Generosity","No","Alot"]],columns=["Correlation with Target","Column Name","Normalised","Outliers"])
delete


# In[82]:


df=df.drop(["Trust (Government Corruption)","Generosity"],axis=1)


# In[83]:


df


# In[94]:


from sklearn.preprocessing import OrdinalEncoder
enc=OrdinalEncoder()


# In[96]:


df.columns


# In[89]:


df.dtypes


# In[101]:


for i in df.columns:
    if df[i].dtypes=="object":    
        df[i]=enc.fit_transform(df[i].values.reshape(-1,1))


# In[102]:


df


# In[103]:


# Removing Outliers
from scipy.stats import zscore


# In[104]:


import numpy as np
z=np.abs(zscore(df))


# In[105]:


z.shape


# In[106]:


z


# In[107]:


# threshold = (-3,3)
#if applied np.abs
threshold = 3

#index number
print(np.where(z>3))


# In[108]:


len(np.where(z>3)[0])


# In[109]:


df_new=df[(z<3).all(axis=1)]


# In[110]:


print("Old Dataframe",df.shape)
print("New Dataframe",df_new.shape)
print("Total Dropped Rows",df.shape[0] - df_new.shape[0])


# In[111]:


# Percentage Data Loss
loss_percent = (158-152)/158*100
print(loss_percent,'%')


# In[112]:


# Model without outliers df

df_new


# In[113]:


#independant Column
x=df_new.iloc[:,:-1]


# In[114]:


#target
y=df_new.iloc[:,-1]


# In[115]:


# Transforming data to remove skewness
from sklearn.preprocessing import power_transform
x=power_transform(x,method='yeo-johnson')
x


# In[116]:


#Using methos Standard Scalar
from sklearn.preprocessing import StandardScaler
#Transform standard normal distribution
sc=StandardScaler()
x=sc.fit_transform(x)
x


# In[117]:


x.mean()


# In[121]:


df.describe()


# In[122]:


df.corr()


# In[123]:


plt.figure(figsize=(22,7))
sns.heatmap(df.corr(),annot=True,linewidths=0.1,linecolor="black",fmt="0.2f")


# In[126]:


import matplotlib.pyplot as plt

plt.figure(figsize=(22,7))
df.corr()['Dystopia Residual'].sort_values(ascending=False).drop(['Dystopia Residual']).plot(kind='bar',color='c')
plt.xlabel('Feature',fontsize=14)
plt.ylabel('Column with target names',fontsize=14)
plt.title('correlation',fontsize=18)
plt.show()


# In[127]:


df.skew()


# In[128]:


#Keeping +/- 0.5


# In[129]:


#Outliers Check
df.dtypes


# In[130]:


df['Country'].plot.box()


# In[131]:


df['Region'].plot.box()


# In[132]:


df['Happiness Rank'].plot.box()


# In[ ]:


df['Happiness Score'].plot.box()


# In[133]:


df['Family'].plot.box()


# In[134]:


df['Freedom'].plot.box()


# In[135]:


df['Dystopia Residual'].plot.box()


# In[136]:


df['Economy (GDP per Capita)'].plot.box()


# In[137]:


df['Health (Life Expectancy)'].plot.box()


# In[139]:


# Removing Outliers
from scipy.stats import zscore
import numpy as np
z=np.abs(zscore(df))
threshold=3
np.where(z>3)


# In[140]:


df_new=df[(z<3).all(axis=1)]


# In[141]:


print("Old Dataframe",df.shape)
print("New Dataframe",df_new.shape)
print("Total Dropped Rows",df.shape[0] - df_new.shape[0])


# In[142]:


# Percentage Data Loss
loss_percent = (158-152)/158*100
print(loss_percent,'%')


# In[143]:


# Model without outliers df

df_new


# In[144]:


from sklearn.preprocessing import MinMaxScaler
mns=MinMaxScaler()
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split


# In[145]:


import warnings
warnings.filterwarnings('ignore')


# In[150]:


for i in range(0,100):
    features_train,features_test,target_train,target_test=train_test_split(x,y,random_state=i,test_size=0.20)
    lr.fit(features_train,target_train)
    pred_train=lr.predict(features_train)
    pred_test=lr.predict(features_test)
    print(f"At Random State{i},the training accuracy is {r2_score(target_train,pred_train)}")
    print(f"At Random State{i},the testing accuracy is {r2_score(target_test,pred_test)}")
    print('\n')


# In[151]:


features_train,features_test,target_train,target_test = train_test_split(x,y,test_size=0.20,random_state=12)


# In[152]:


lr.fit(features_train,target_train)


# In[153]:


pred_test=lr.predict(features_test)


# In[154]:


print(r2_score(target_test,pred_test))


# In[155]:


#Cross Validation score for logistic regression


# In[157]:


Train_accuracy=r2_score(target_train,pred_train)
Test_accuracy=r2_score(target_test,pred_test)


# In[158]:


from sklearn.model_selection import cross_val_score


# In[160]:


for j in range(2,10):
    lsscore = cross_val_score(lr,x,y,cv=j)
    lsc=lsscore.mean()
    print("At CV:-",j)
    print("Cross Validation Score is:-",lsc*100)
    print("accuracy Score for training is:-",Train_accuracy*100)
    print("accuracy Score for test is:-",Test_accuracy*100)
    print("\n")


# In[162]:


lsscore_selected = cross_val_score(lr,x,y,cv=7).mean()
print("The CV Score is:",lsscore_selected,"\n The accuracy score is:",Test_accuracy)


# In[163]:


# AUC ROC Curve:


# In[165]:


import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
plt.scatter(x=target_test,y=pred_test,color='r')
plt.plot(target_test,pred_test,color='b')
plt.xlabel('Actual Value',fontsize=14)
plt.ylabel('Predicted Value',fontsize=14)
plt.title('Linear Regression',fontsize=18)
plt.show()


# In[167]:


#Model Saving

import pickle
filename = 'World_Happiness_pk1'
pickle.dump(lr,open(filename,'wb'))


# In[168]:


# Conclusion:

import numpy as np
a=np.array(y_test)
predicted = np.array(lr.predict(x_test))
df_com=pd.DataFrame({"origional":a,"predicted":predicted},index=range(len(a)))
df_com


# In[ ]:




