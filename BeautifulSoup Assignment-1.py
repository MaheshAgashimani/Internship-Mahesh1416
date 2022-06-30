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


#Assignment-Q1
page1 = requests.get("https://www.wikipedia.org")


# In[5]:


page1


# In[6]:


soup1 = BeautifulSoup(page1.content)
soup1


# In[7]:


Header = soup1.find('div',class_="central-featured-lang lang1")
Header


# In[8]:


Header.text


# In[9]:


Header.text.split()


# In[10]:


Header.text.split()[0]


# In[11]:


Header1 = []

for i in soup1.find_all('div',class_="central-featured"):
    Header1.append(i.text)


# In[12]:


Header1


# In[13]:


#Assignment-Q2
page2 = requests.get("https://www.imdb.com/search/title/?groups=top_100")


# In[14]:


page2


# In[15]:


soup2 = BeautifulSoup(page2.content)
soup2


# In[16]:


Name = soup2.find('h3', class_="lister-item-header")
Name


# In[17]:


#For Multiple Names
Name = []
for i in soup2.find_all('h3', class_="lister-item-header"):
    Name.append(i.text)


# In[18]:


#For Multiple Names
Rating = []
for i in soup2.find_all('div', class_="ratings-bar"):
    Rating.append(i.text)


# In[19]:


Name


# In[20]:


Rating


# In[21]:


Year = []
for i in soup2.find_all('span', class_="lister-item-year text-muted unbold"):
    Year.append(i.text)


# In[22]:


Year


# In[23]:


print(len(Name),len(Rating),len(Year))


# In[24]:


import pandas as pd


# In[25]:


import pandas as pd
df = pd.DataFrame({'Names':Name,'Ratings':Rating,'Years':Year})
df


# In[26]:


#Assignment-Q3


# In[27]:


page3 = requests.get("https://www.imdb.com/list/ls009997493")


# In[28]:


page3


# In[29]:


soup3 = BeautifulSoup(page3.content)
soup3


# In[31]:


#For Multiple Names
IndiaName = []
for i in soup3.find_all('h3', class_="lister-item-header"):
    IndiaName.append(i.text)


# In[32]:


IndiaName


# In[33]:


IndiaRating = []
for i in soup3.find_all('div', class_="ipl-rating-star small"):
    IndiaRating.append(i.text)


# In[34]:


IndiaRating


# In[35]:


IndiaYear = []
for i in soup3.find_all('span', class_="lister-item-year text-muted unbold"):
    IndiaYear.append(i.text)


# In[36]:


IndiaYear


# In[37]:


print(len(IndiaName),len(IndiaRating),len(IndiaYear))


# In[38]:


import pandas as pd
import pandas as pd
df = pd.DataFrame({'Names':IndiaName,'Ratings':IndiaRating,'Years':IndiaYear})
df


# In[39]:


#Assignment - Q4


# In[40]:


page4 = requests.get("https://presidentofindia.nic.in/former-presidents.htm")


# In[41]:


page4


# In[42]:


soup4 = BeautifulSoup(page4.content)
soup4


# In[43]:


# Response is gretarer than 200


# In[44]:


#Assignment - Q5


# In[45]:


page5 = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")


# In[46]:


page5


# In[47]:


soup5 = BeautifulSoup(page5.content)
soup5


# In[48]:


Team = soup5.find('span',class_="u-hide-phablet")
Team.text


# In[49]:


Matches = soup5.find('td',class_="table-body__cell u-center-text")
Matches.text


# In[50]:


Rating = soup5.find('td',class_="table-body__cell u-text-right rating")
Rating.text


# In[51]:


Team1 = soup5.find('td',class_="rankings-block__banner--team-name")
Team1.text


# In[52]:


Points = soup5.find('td',class_="rankings-block__banner--points")
Points.text


# In[53]:


TeamName = []
for i in soup5.find_all('span',class_="u-hide-phablet"):
    TeamName.append(i.text)


# In[54]:


TeamName


# In[55]:


Matches = []
for i in soup5.find_all('td',class_="table-body__cell u-center-text"):
    Matches.append(i.text)


# In[56]:


Matches


# In[57]:


Rating1 = []
for i in soup5.find_all('td',class_="table-body__cell u-text-right rating"):
    Rating1.append(i.text)


# In[58]:


Rating1


# In[59]:


print (len(TeamName),len(Matches),len(Rating1))


# In[60]:


import pandas as pd
df = pd.DataFrame({'TeamName':TeamName,'Matches':Matches,'Rating1':Rating1})
df


# In[61]:


#Men Batsman
Menpage5 = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi")
Menpage5


# In[62]:


Menpage5


# In[63]:


Mensoup5 = BeautifulSoup(Menpage5.content)
Mensoup5


# In[64]:


PlayerName = Mensoup5.find('td',class_="table-body__cell name")
PlayerName.text


# In[65]:


PlayerName1 = []
for i in Mensoup5.find_all('td',class_="table-body__cell name"):
    PlayerName1.append(i.text)


# In[66]:


PlayerName1


# In[67]:


TeamName1 = []
for i in Mensoup5.find_all('td',class_="table-body__cell nationality-logo"):
    TeamName1.append(i.text)


# In[68]:


TeamName1


# In[69]:


Rating1 = []
for i in Mensoup5.find_all('td',class_="table-body__cell u-text-right rating"):
    Rating1.append(i.text)


# In[70]:


Rating1


# In[71]:


print(len(PlayerName1),len(TeamName1),len(Rating1))


# In[72]:


import pandas as pd
df = pd.DataFrame({'PlayerName':PlayerName1,'TeamName':TeamName1,'Rating':Rating1})
df


# In[73]:


# Men Bowling
MenBowlpage5 = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling")
MenBowlpage5


# In[74]:


MenBowlsoup5 = BeautifulSoup(MenBowlpage5.content)
MenBowlsoup5


# In[75]:


PlayerName1 = []
for i in MenBowlsoup5.find_all('td',class_="table-body__cell rankings-table__name name"):
    PlayerName1.append(i.text)


# In[76]:


PlayerName1


# In[77]:


TeamName1 = []
for i in MenBowlsoup5.find_all('td',class_="table-body__cell nationality-logo rankings-table__team"):
    TeamName1.append(i.text)


# In[78]:


TeamName1


# In[79]:


Rating1 = []
for i in MenBowlsoup5.find_all('td',class_="table-body__cell rating"):
    Rating1.append(i.text)


# In[80]:


Rating1


# In[81]:


print(len(PlayerName1),len(TeamName1),len(Rating1))


# In[82]:


import pandas as pd
df = pd.DataFrame({'PlayerName':PlayerName1,'TeamName':TeamName1,'Rating':Rating1})
df


# In[83]:


#Assignment - Q6


# In[84]:


Womenpage5 = requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")


# In[85]:


Womenpage5


# In[87]:


Womensoup5 = BeautifulSoup(Womenpage5.content)
Womensoup5


# In[88]:


first_data=Womensoup5.find("div",class_="rankings-block__top-player")


# In[89]:


TeamName = []
for i in Womensoup5.find_all('span',class_="u-hide-phablet"):
    TeamName.append(i.text)


# In[90]:


TeamName


# In[91]:


Matches = []
for i in Womensoup5.find_all('td',class_="table-body__cell u-center-text"):
    Matches.append(i.text)


# In[92]:


Matches


# In[93]:


Rating = []
for i in Womensoup5.find_all('td',class_="table-body__cell u-text-right rating"):
    Rating.append(i.text)


# In[94]:


Rating


# In[95]:


print (len(TeamName),len(Matches),len(Rating))


# In[96]:


import pandas as pd
df = pd.DataFrame({'TeamName':TeamName,'Matches':Matches,'Rating':Rating})
df


# In[97]:


#Women Batsman
WomenBatsmanpage5 = requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi")
WomenBatsmanpage5


# In[98]:


WomenBatsmansoup5 = BeautifulSoup(WomenBatsmanpage5.content)
WomenBatsmansoup5


# In[99]:


PlayerName1 = []
for i in WomenBatsmansoup5.find_all('td',class_="table-body__cell name"):
    PlayerName1.append(i.text)


# In[100]:


PlayerName1


# In[101]:


TeamName1 = []
for i in WomenBatsmansoup5.find_all('td',class_="table-body__cell nationality-logo"):
    TeamName1.append(i.text)


# In[102]:


TeamName1


# In[103]:


Rating1 = []
for i in WomenBatsmansoup5.find_all('td',class_="table-body__cell u-text-right rating"):
    Rating1.append(i.text)


# In[104]:


Rating1


# In[105]:


print(len(PlayerName1),len(TeamName1),len(Rating1))


# In[106]:


import pandas as pd
df = pd.DataFrame({'PlayerName':PlayerName1,'TeamName':TeamName1,'Rating':Rating1})
df


# In[107]:


#Women Bowler
WomenBowlpage5 = requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/bowling")
WomenBowlpage5


# In[108]:


WomenBowlsoup5 = BeautifulSoup(WomenBowlpage5.content)
WomenBowlsoup5


# In[109]:


PlayerName1 = []
for i in WomenBowlsoup5.find_all('td',class_="table-body__cell rankings-table__name name"):
    PlayerName1.append(i.text)


# In[110]:


PlayerName1


# In[111]:


TeamName1 = []
for i in WomenBowlsoup5.find_all('td',class_="table-body__cell nationality-logo rankings-table__team"):
    TeamName1.append(i.text)


# In[112]:


TeamName1


# In[113]:


Rating1 = []
for i in WomenBowlsoup5.find_all('td',class_="table-body__cell rating"):
    Rating1.append(i.text)


# In[114]:


Rating1


# In[115]:


print(len(PlayerName1),len(TeamName1),len(Rating1))


# In[116]:


import pandas as pd
df = pd.DataFrame({'PlayerName':PlayerName1,'TeamName':TeamName1,'Rating':Rating1})
df


# In[117]:


# Assignment - Q7


# In[118]:


r1 = requests.get("https://www.cnbc.com/world/?region=world")
coverpage = r1.content


# In[119]:


soup6 = BeautifulSoup(coverpage, 'html5lib')


# In[120]:


coverpage_news.text


# In[121]:


# Assignment - Q8


# In[122]:


page8 = requests.get("https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles")


# In[123]:


page8


# In[124]:


soup8 = BeautifulSoup(page8.content)
soup8


# In[125]:


Articles = soup8.find('h2',class_="sc-1qrq3sd-1 MKjKb sc-1nmom32-0 sc-1nmom32-1 hqhUYH ebTA-dR")
Articles


# In[126]:


Articles1 = []
for i in soup8.find_all('h2',class_="sc-1qrq3sd-1 MKjKb sc-1nmom32-0 sc-1nmom32-1 hqhUYH ebTA-dR"):
    Articles1.append(i.text)


# In[127]:


Articles1


# In[128]:


Author = []
for i in soup8.find_all('span',class_="sc-1w3fpd7-0 pgLAT"):
    Author.append(i.text)


# In[129]:


Author


# In[130]:


Published = []
for i in soup8.find_all('span',class_="sc-1thf9ly-2 bKddwo"):
    Published.append(i.text)


# In[131]:


Published


# In[132]:


PaperURL = []
for i in soup8.find_all('a',class_="sc-5smygv-0 nrDZj"):
    PaperURL.append(i['href'])


# In[133]:


PaperURL


# In[134]:


print(len(Articles1),len(Author),len(Published),len(PaperURL))


# In[135]:


import pandas as pd
df = pd.DataFrame({'Articles1':Articles1,'Author':Author,'Published':Published,'PaperURL':PaperURL})


# In[136]:


df


# In[137]:


#Assignment - Q9


# In[138]:


page9 = requests.get("https://www.dineout.co.in")


# In[139]:


page9


# In[140]:


soup9 = BeautifulSoup(page9.content)
soup9


# In[141]:


RestName = soup9.find('h4',class_="_1jbOb")
RestName.text


# In[142]:


RestLocation = soup9.find('p',class_="_1jbOb")
RestLocation.text


# In[143]:


RestRating = soup9.find('div',class_="kGUdK _1oTbl")
RestRating


# In[144]:


RestRating.text


# In[147]:


RestCuisine = soup9.find('a',class_="about-info d-flex")


# In[148]:


RestCuisine


# In[149]:


RestCuisine1 = []
for i in soup9.find_all('div',class_="about-info d-flexp"):
    RestCuisine1.append(i['href'])


# In[150]:


RestCuisine1


# In[151]:


image = []

for i in soup9.find_all('img',class_="no-img"):
    image.append(i['data-src'])


# In[152]:


image


# In[153]:


RestName = []
for i in soup9.find_all('h4',class_="_1jbOb"):
    RestName.append(i.text)


# In[154]:


RestName


# In[155]:


RestLocation1 = []
for i in soup9.find_all('p',class_="_1jbOb"):
    RestLocation1.append(i.text)


# In[156]:


RestLocation1


# In[157]:


RestRating1 = []
for i in soup9.find_all('div',class_="kGUdK _1oTbl"):
    RestRating1.append(i.text)


# In[158]:


RestRating1


# In[159]:


print(len(RestName),len(RestLocation1),len(RestRating1))


# In[160]:


import pandas as pd
df = pd.DataFrame({'RestName':RestName,'RestLocation':RestLocation1,'RestRating':RestRating1})
df


# In[161]:


# Assignment -Q10


# In[162]:


page10 = requests.get("https://scholar.google.com/citations?view_op=top_venues&hl=en")


# In[163]:


page10


# In[164]:


soup10 = BeautifulSoup(page10.content)
soup10


# In[165]:


Rank = []

for i in soup10.find_all('td',class_="gsc_mvt_p"):
    Rank.append(i.text)


# In[166]:


Rank


# In[167]:


Publication = []

for i in soup10.find_all('td',class_="gsc_mvt_t"):
    Publication.append(i.text)


# In[168]:


Publication


# In[169]:


h5Index = []

for i in soup10.find_all('td',class_="gsc_mvt_n"):
    h5Index.append(i.text)


# In[170]:


h5Index


# In[171]:


h5Median = []

for i in soup10.find_all('span',class_="gs_ibl gsc_mp_anchor"):
    h5Median.append(i.text)


# In[172]:


h5Median


# In[173]:


print (len(Rank),len(Publication),len(h5Index),len(h5Median))


# In[174]:


import pandas as pd
df = pd.DataFrame({'Rank':Rank,'Publication':Publication,'h5Index':h5Index,'h5Median':h5Median})
df


# In[175]:


#Assignment - Q7


# In[177]:


page7 = requests.get("https://www.cnbc.com/world/?region=world")


# In[178]:


page7


# In[179]:


soup7 = BeautifulSoup(page7.content)
soup7


# In[180]:


Headline = soup7.find('div', class_="RiverHeadline-headline RiverHeadline-hasThumbnail")


# In[181]:


Headline


# In[184]:


Headline1 = []
for i in soup7.find_all('div',class_="RiverHeadline-headline RiverHeadline-hasThumbnail"):
    Headline1.append(i.text)


# In[185]:


Headline1


# In[189]:


Time = []
for i in soup7.find_all('span',class_="RiverByline-datePublished"):
    Time.append(i.text)


# In[190]:


Time


# In[215]:


NewsLink = []
for i in soup7.find_all('div',class_="RiverHeadline-headline RiverHeadline-hasThumbnail"):
    NewsLink.append(i.text)


# In[216]:


NewsLink


# In[217]:


print(len(Headline1),len(Time),len(NewsLink))


# In[219]:


import pandas as pd
df = pd.DataFrame({'Headline1':Headline1,'Time':Time,'NewsLink':NewsLink})
df


# In[ ]:




