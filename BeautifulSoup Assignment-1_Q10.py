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


page10 = requests.get("https://scholar.google.com/citations?view_op=top_venues&hl=en")


# In[5]:


page10


# In[6]:


soup10 = BeautifulSoup(page10.content)
soup10


# In[8]:


Rank = []

for i in soup10.find_all('td',class_="gsc_mvt_p"):
    Rank.append(i.text)


# In[9]:


Rank


# In[10]:


Publication = []

for i in soup10.find_all('td',class_="gsc_mvt_t"):
    Publication.append(i.text)


# In[11]:


Publication


# In[12]:


h5Index = []

for i in soup10.find_all('td',class_="gsc_mvt_n"):
    h5Index.append(i.text)


# In[13]:


h5Index


# In[15]:


h5Median = []

for i in soup10.find_all('span',class_="gs_ibl gsc_mp_anchor"):
    h5Median.append(i.text)


# In[16]:


h5Median


# In[17]:


print (len(Rank),len(Publication),len(h5Index),len(h5Median))


# In[18]:


import pandas as pd
df = pd.DataFrame({'Rank':Rank,'Publication':Publication,'h5Index':h5Index,'h5Median':h5Median})


# In[ ]:




