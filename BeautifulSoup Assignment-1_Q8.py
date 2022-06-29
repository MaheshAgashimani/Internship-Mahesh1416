#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')


# In[2]:


get_ipython().system('pip install requests')


# In[3]:


from bs4 import BeautifulSoup
import requests


# In[4]:


page8 = requests.get("https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles")


# In[5]:


page8


# In[6]:


soup8 = BeautifulSoup(page8.content)
soup8


# In[8]:


Articles = soup8.find('h2',class_="sc-1qrq3sd-1 MKjKb sc-1nmom32-0 sc-1nmom32-1 hqhUYH ebTA-dR")
Articles


# In[11]:


Articles1 = []
for i in soup8.find_all('h2',class_="sc-1qrq3sd-1 MKjKb sc-1nmom32-0 sc-1nmom32-1 hqhUYH ebTA-dR"):
    Articles1.append(i.text)


# Articles1

# In[12]:


Articles1


# In[13]:


Author = []
for i in soup8.find_all('span',class_="sc-1w3fpd7-0 pgLAT"):
    Author.append(i.text)


# In[14]:


Author


# In[15]:


Published = []
for i in soup8.find_all('span',class_="sc-1thf9ly-2 bKddwo"):
    Published.append(i.text)


# In[16]:


Published


# In[21]:


PaperURL = []
for i in soup8.find_all('a',class_="sc-5smygv-0 nrDZj"):
    PaperURL.append(i['href'])


# In[22]:


PaperURL


# In[23]:


print(len(Articles1),len(Author),len(Published),len(PaperURL))


# In[26]:


import pandas as pd
df = pd.DataFrame({'Articles1':Articles1,'Author':Author,'Published':Published,'PaperURL':PaperURL})


# In[27]:


df


# In[ ]:




