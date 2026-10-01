#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing libraries that allow data sets to be imported, processed, and create visualizations
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
#libraries imported and setup seaborn library style as whitegrid


# In[2]:


#import Weather station datasets for Seattle and Detroit
df_seattle = pd.read_csv(
    'https://raw.githubusercontent.com/Ninofo/Weather/refs/heads/main/seattle_rain.csv'
)
df_detroit = pd.read_csv(
    'https://raw.githubusercontent.com/Ninofo/Weather/refs/heads/main/Detroit_rain.csv'
)
#imported datasets from Github repository 


# In[3]:


#Exploring datasets for both seattle and Detroit weather stations
type(df_seattle)


# In[4]:


df_seattle.head()


# In[5]:


df_detroit.head()


# In[6]:


df_seattle.columns


# In[7]:


df_detroit.columns


# In[8]:


df_seattle.info()


# In[9]:


df_detroit.info()


# In[10]:


print(df_seattle.shape)


# In[11]:


print(df_detroit.shape)


# In[12]:


df_detroit['STATION']


# In[13]:


df_detroit['STATION'].unique()


# In[14]:


df_seattle['STATION'].unique()
#


# In[15]:


df_detroit['DATE']
#Discovered Seattle dataFrame has more columns than Detroit dataFrame, Detroit dataFrame has more rows, both datasets include only one weather station, and both have common column of 'DATE' that is a string datatype


# In[16]:


#converting 'DATE' data type from string to dateTime datatype in both dataFrames
df_seattle['DATE'] = pd.to_datetime(df_seattle['DATE'])


# In[17]:


df_detroit['DATE']=pd.to_datetime(df_detroit['DATE'])


# In[18]:


df_seattle['DATE'].agg(['min','max'])


# In[19]:


df_detroit['DATE'].agg(['min','max'])
#converted 'Date' column values from string to dateTime datatype and confirmed only intended dates were included in the date range


# In[20]:


#visualize seattle and Detroit dataFrames separately to quickly scan for any gaps in data
plt.figure(figsize=(20,5))
sns.lineplot(data=df_seattle, x='DATE', y='PRCP')
plt.xlabel("Date", fontsize=18)
plt.ylabel("precipitation (inches)", fontsize = 18)
plt.tick_params(labelsize=15)
plt.show()


# In[21]:


plt.figure(figsize=(20,5))
sns.lineplot(data=df_detroit, x='DATE', y='PRCP')
plt.xlabel("Date", fontsize=18)
plt.ylabel("precipitation (inches)", fontsize = 18)
plt.tick_params(labelsize=15)
plt.show()
#Seattle dataFrame appears to be missing data in the beginning of 2018 while Detroit DataFrame was larger but did not appear to have any missing data


# In[22]:


#join 'DATE' and 'PRCP' subsections from Detroit and Seattle DataFrames together to create a new dataFrame
df = df_detroit[['DATE', 'PRCP']].merge(df_seattle[['DATE','PRCP']], on='DATE', how='outer')


# In[23]:


df.head()
#confirmed merge of subsections into a new dataFrame 


# In[24]:


#Convert dataFrame from wide to tidy 
df=pd.melt(df, id_vars='DATE', var_name='city', value_name='precipitation')


# In[25]:


df.head()
#confirmed conversion of wide dataFrame to tidy dataFrame. Resulted in precipitation values from each dataFrame being differentiated by suffix '_x' and '_y'


# In[26]:


#rename city values to more clearly show which city's weather station collected the value
df.loc[df['city'] == 'PRCP_x', 'city'] = 'DTW'


# In[27]:


df.loc[df['city']=='PRCP_y', 'city']='SEA'


# In[28]:


df.head()


# In[29]:


df.tail()
#confirmed value representation changed. DTW = Detroit Airport and SEA = Seattle Airport


# In[30]:


#make DATE column Header lowercase
df = df.rename(columns = {'DATE': 'date'})


# In[31]:


df.head()
#confirmed Date column Header became lowercase


# In[32]:


#Identifying Missing/Null Values 
df.info()


# In[33]:


df.notna().sum()


# In[34]:


df.isna().sum()


# In[35]:


df.loc[df['city'] == 'SEA', 'precipitation'].isna().sum()


# In[36]:


df.loc[df['city']=='DTW', 'precipitation'].isna().sum()
#Found 190 null precipitation values that all originated from the Seattle dataFrame


# In[37]:


#filling in missing precipitation values with precipitation mean of other years available for the missing date.
df['day_of_year'] = pd.DatetimeIndex(df['date']).day_of_year


# In[38]:


df.head()


# In[39]:


df.tail()


# In[40]:


mean_day_precipitation = df.loc[
    df['city'] == 'SEA',
    ['precipitation', 'day_of_year']
    ].groupby(
        'day_of_year'
    ).mean()


# In[41]:


plt.figure(figsize=(20,5))
sns.lineplot(
    data = mean_day_precipitation, 
    x = 'day_of_year',
    y = 'precipitation')
plt.xlabel('Day of the year', fontsize =18)
plt.ylabel('Mean percipitation (inches)', fontsize=18)
plt.tick_params(labelsize=15)
plt.show()
#this particular cell only provides visualization for the mean percipitation of a given day in a year


# In[42]:


df['precipitation'].isna() ==True


# In[43]:


indices = np.where(df['precipitation'].isna() == True)[0]


# In[44]:


print(indices) #only serves to confirm indices created intended array


# In[45]:


for index in indices:
    df.loc[index, 'precipitation']= mean_day_precipitation.loc[df.loc[index, 'day_of_year']].values[0]


# In[46]:


df.isna().sum() #serves only to confirm there are no more missing values 
#created new column in dataFrame linking the same date in every year to each other.
#The new column to allows and index to be created relating the same dates in every available year and their mean precipitation values. 
#A for loop utilizes this index to iterate over each missing value in precipitation column and replace it with the mean precipitation


# In[ ]:




