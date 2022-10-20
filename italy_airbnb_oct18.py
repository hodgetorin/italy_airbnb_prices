#!/usr/bin/env python
# coding: utf-8

# df was already filtered in excel for:
# price between 30 and 250
# room type = home/whole apt
# all cities

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("italy.csv")


# In[3]:


df.head()


# In[55]:


df.describe()


# Null Hypothesis:
# The mean price of the cities are equal, there is no variation.
# 
# Alt Hypothesis:
# at least one group mean is different. All means are not equal.
# 

# In[5]:


df.drop_duplicates()


# In[6]:


df_list = []

cities = ['Bergamo', 'Bologna', 'Florence', 'Milan', 'Naples', 'Puglia', 'Rome', 'Sicily', 'Trentino', 'Venice']

for i in (range(0,10)):
    city = df[df['City']==cities[i]]
    temp = city.sample(n=300, random_state=5)
    print("line ", i)
    print(temp.nunique())
    df_list.append(temp)

df_s = pd.concat(df_list)


# In[7]:


#df_s.set_index('id')
df_ss = df_s.pivot_table(index='id', columns='City', values='price')
df_ss.head()


# In[ ]:





# In[8]:


df_s.count()


# In[12]:


import seaborn as sns

corr = df_ss.corr()
sns.heatmap(corr,vmin=-1, vmax=1, annot=True)

# alright given this table below, we can pick and choose a few pairs of cities to compare using t-test


# In[59]:


# Find the population mean
mu = df['price'].mean()
sd = df['price'].std()
mu


# In[53]:


from statsmodels.stats.weightstats import ztest as ztest

tests = []

# perform one sample z-test for each city against the population mean:
for i in (range(0,10)):
    t, p = ztest(df[df['City']==cities[i]]['price'], value=mu)
    city_mean = df[df['City']==cities[i]]['price'].mean()
    temp = [cities[i], t, p, city_mean]
    tests.append(temp)

tests


# In[62]:


# fit these into a dataframe:

df_results = pd.DataFrame(tests)
df_results.columns = ['city', 'test-statistic', 'p-value', 'mean price (€)']

df_results.sort_values('mean price (€)', ascending=False)


# In[41]:





# In[42]:





# In[ ]:




