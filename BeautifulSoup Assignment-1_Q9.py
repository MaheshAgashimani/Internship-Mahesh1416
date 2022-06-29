#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install bs4')


# In[4]:


get_ipython().system('pip install requests')


# In[5]:


from bs4 import BeautifulSoup
import requests


# In[6]:


page9 = requests.get("https://www.dineout.co.in")


# In[7]:


page9


# In[8]:


soup9 = BeautifulSoup(page9.content)
soup9


# In[9]:


RestName = soup9.find('h4',class_="_1jbOb")
RestName.text


# In[10]:


RestLocation = soup9.find('p',class_="_1jbOb")
RestLocation.text


# In[11]:


RestRating = soup9.find('div',class_="kGUdK _1oTbl")
RestRating


# In[12]:


RestRating.text


# In[14]:


RestCuisine = soup9.find('a',class_="about-info d-flex")
RestCuisine


# In[41]:


RestCuisine1 = []
for i in soup9.find_all('div',class_="about-info d-flexp"):
    RestCuisine1.append(i['href'])


# In[43]:


RestCuisine1


# In[40]:


image = []

for i in soup9.find_all('img',class_="no-img"):
    image.append(i['data-src'])


# In[25]:


image


# In[56]:


print(len(),len(),len())


# In[29]:


RestName = []
for i in soup9.find_all('h4',class_="_1jbOb"):
    RestName.append(i.text)


# In[30]:


RestName


# In[31]:


RestLocation1 = []
for i in soup9.find_all('p',class_="_1jbOb"):
    RestLocation1.append(i.text)


# In[32]:


RestLocation1


# In[33]:


RestRating1 = []
for i in soup9.find_all('div',class_="kGUdK _1oTbl"):
    RestRating1.append(i.text)


# In[34]:


RestRating1


# In[35]:


print(len(RestName),len(RestLocation1),len(RestRating1))


# In[47]:


import pandas as pd
df = pd.DataFrame({'RestName':RestName,'RestLocation':RestLocation1,'RestRating':RestRating1})


# In[48]:


df


# In[ ]:




