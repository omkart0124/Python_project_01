#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# # About Covid-19

# In[14]:


from IPython.display import Image
Image(r'C:\Users\thora\.ipynb_checkpoints\New folder/coimage.jpg')


# # What is covid-19..??

# In[15]:


# COVID-19 is the disease caused by a new coronavirus called SARS-CoV-2. WHO first learned of this new virus on 31 December 2019, 
# following a report of a cluster of cases of ‘viral pneumonia’ in Wuhan, People’s Republic of China.


# # What happens to people who get covid-19.. ??

# In[16]:


# Among those who develop symptoms, most (about 80%) recover from the disease without needing hospital treatment. 
# About 15% become seriously ill and require oxygen and 5% become critically ill and need intensive care.
# Complications leading to death may include respiratory failure, acute respiratory distress syndrome (ARDS), 
# sepsis and septic shock, thromboembolism, and/or multiorgan failure, including injury of the heart, liver or kidneys.
# In rare situations, children can develop a severe inflammatory syndrome a few weeks after infection. 


# # About vaccines

# In[17]:


from IPython.display import Image
Image(r'C:\Users\thora\.ipynb_checkpoints\New folder/vaccines.jpg')


# # What is in vaccine..??

# In[6]:


# All the ingredients of a vaccine play an important role in ensuring a vaccine is safe and effective. Some of these include:
# The antigen. This is a killed or weakened form of a virus or bacteria, which trains our bodies to recognize and fight the 
# disease if we encounter it in the future.
# Adjuvants, which help to boost our immune response. This means they help vaccines to work better.
# Preservatives, which ensure a vaccine stays effective.
# Stabilisers, which protect the vaccine during storage and transportation.
# Vaccine ingredients can look unfamiliar when they are listed on a label. However, many of the components used in vaccines
# occur naturally in the body, in the environment, and in the foods we eat. All of the ingredients in vaccines – as well as 
# the vaccines themselves - are thoroughly tested and monitored to ensure they are safe.


# # How does vaccine work..??

# In[7]:


# Vaccines reduce risks of getting a disease by working with your body’s natural defenses to build protection. 
# When you get a vaccine, your immune system responds. It:
# Recognizes the invading germ, such as the virus or bacteria.
# Produces antibodies. Antibodies are proteins produced naturally by the immune system to fight disease.
# Remembers the disease and how to fight it. If you are then exposed to the germ in the future, 
# your immune system can quickly destroy it before you become unwell.


# # About Vaccination

# In[8]:


from IPython.display import Image
Image(r'C:\Users\thora\.ipynb_checkpoints\New folder/CovidVaccination.jpg')


# # What is Vaccination..??

# In[9]:


# Vaccination is a simple, safe, and effective way of protecting people against harmful diseases, before they come into 
# contact with them. It uses your body’s natural defenses to build resistance to specific infections and makes your 
# immune system stronger.
# Vaccines train your immune system to create antibodies, just as it does when it’s exposed to a disease. 
# However, because vaccines contain only killed or weakened forms of germs like viruses or bacteria, they do not cause
# the disease or put you at risk of its complications.
# Most vaccines are given by an injection, but some are given orally (by mouth) or sprayed into the nose.


# In[10]:


# To bring this pandemic to an end, a large share of the world needs to be immune to the virus. The safest way to achieve this
# is with a vaccine. Vaccines are a technology that humanity has often relied on in the past to bring down the death toll of 
# infectious diseases.

# Within less than 12 months after the beginning of the COVID-19 pandemic, several research teams rose to the challenge 
# and developed vaccines that protect from SARS-CoV-2, the virus that causes COVID-19.

# Now the challenge is to make these vaccines available to people around the world. It will be key that people in 
# all countries — not just in rich countries — receive the required protection. 


# In[11]:


# Healthcare personnel and residents of long-term care facilities should be offered the first doses of COVID-19 vaccines


# In[ ]:





# In[ ]:





# #                                COVID-19 World Vaccination Progress

# # Content

# In[12]:


''''The data contains the following information:

1. Country :- this is the country for which the vaccination information is provided;

2. ISO Code :- ISO code for the country;

3. Date :- date for the data entry total vaccination done Till 20th January.
   
4. Total number of vaccinations :- this is the absolute number of total immunizations in the country;

5. people vaccinated :- a person, depending on the immunization scheme, will receive 
   one or more (typically 2) vaccines; at a certain moment, the number of vaccination might be larger 
   than the number of people;

6. people fully vaccinated :- this is the number of people that received the entire set
   of immunization according to the immunization scheme (typically 2); at a certain moment in time, there 
   might be a certain number of people that received one vaccine and another number (smaller) of people 
   that received all vaccines in the scheme;
   
7. Daily vaccinations (raw) :- for a certain data entry, the number of vaccination for that date/country;

8. Daily vaccinations :- for a certain data entry, the number of vaccination for that date/country;

9. Total vaccinations per hundred :- ratio (in percent) between vaccination number and total population 
   up to the date in the country;
   
10. people vaccinated per hundred :- ratio (in percent) between population immunized and total population
    up to the date in the country;
    
11. people fully vaccinated per hundred :- ratio (in percent) between population fully immunized and total
    population up to the date in the country;

13. Daily vaccinations per million :- ratio (in ppm) between vaccination number and total population for the 
    current date in the country;
    
14. Vaccines :- total number of vaccines used in the country (up to date);

15. Source name :- source of the information (national authority, international organization, local organization etc.);

16. Source website :- website of the source of information;''''


# In[18]:


covid=pd.read_csv(r"C:\Users\thora\.ipynb_checkpoints\New folder\\covid_data.csv")
# this 'r' will remove if there any unicode error


# In[19]:


covid                                                                                   # here my data successfully restored
                                                                                        # it has 39 rows and 15 columns


# # 1. Use describe( )

# In[20]:


covid.describe()
# it returns all statistics of numeric columns(int,float..)


# # 2. vaccines with names

# In[21]:


covid['vaccines'].unique()                                                                          # total vaccines with name


# # 3. find all the null values in data

# In[22]:


covid.isnull()
# isnull() function detect missing values in the given series object. It return a boolean same-sized object indicating
# if the values are NA. Missing values gets mapped to True and non-missing value gets mapped to False .


# In[23]:


covid.notnull()
# notnull. Detect non-missing values for an array-like object. This function takes a scalar or array-like object and indictates
# whether values are valid (not missing, which is NaN in numeric arrays, None or NaN in object arrays, NaT in datetimelike


# # 4. Which countries use 'Sputnik V'  vaccine to vaccinate people

# In[24]:


# Getting 'Sputnik V' data
covid[covid['vaccines'] == 'Sputnik V'] 
#  Filtering


# # 5. Rename vaccines to vac

# In[25]:


covid.rename(columns = {'vaccines' : 'vac'}, inplace = True)


# In[26]:


covid.head(1)


# In[57]:


covid.rename(columns = {'vac' : 'vaccines'}, inplace = True)


# In[28]:


covid.head(1)


# # 6. Contain all source name of 'Ministry of Health' (using str.contains)

# In[29]:


covid[covid['source_name'].str.contains('Ministry of Health')]


# # 7. Find 'people_fully_vaccinated' > 1000000 & Which country use 'Pfizer/BioNTech' vaccine to vaccinate people

# In[30]:


# Using '&' operator--(covid['vaccines'] == 'Pfizer/BioNTech')]
covid[(covid['people_fully_vaccinated'] > 1000000) & (covid['vaccines'] == 'Pfizer/BioNTech')]


# # 8. Find the number of times 'people_vaccinated > 10000000'

# In[31]:


covid[covid['people_vaccinated'] > 10000000]
# and here we have all the data when ['people_vaccinated'] > 10000000]


# # 9. What is the mean, median, standard deviation and variance of        'people_vaccinated_per_hundred'

# In[32]:


covid.people_vaccinated_per_hundred.mean()


# In[33]:


covid.people_vaccinated_per_hundred.median()


# In[34]:


covid.people_vaccinated_per_hundred.std()


# In[35]:


covid.people_vaccinated_per_hundred.var()


# # 10. Extract 'Argentina' data

# In[36]:


Argentina=covid[covid['country']=='Argentina']
# Extracting Argentina data


# In[37]:


Argentina


# # 11. Which vaccines are used and in which countries?

# In[38]:


vacc=covid[['country','vaccines']]


# In[39]:


vacc


# # 12. Which country is vaccinated more people?

# In[40]:


total_vaccinations=covid.groupby("country")["total_vaccinations"].sum()
total_vaccinations


# In[41]:


sorted_vaccines_df=covid.sort_values('people_fully_vaccinated',ascending=False)
sorted_vaccines_df.head(3)


# # 13. Highlight columns

# In[42]:


def highlight_col(x):
    r = 'background-color: red'
    y = 'background-color: yellow'#          color for columns
    g = 'background-color: grey'
    temp_df=pd.DataFrame('',index=x.index, columns=x.columns)
    temp_df.iloc[:,3] = r
    temp_df.iloc[:,4] = y
    temp_df.iloc[:,5] = g
    return temp_df

sorted_vaccines_df.style.apply(highlight_col, axis=None)


# In[ ]:





# # Graphs
# 1. Scatterplot
# 2. Pairplot
# 3. Pie chart
# 4. Histogram(Distplot)
# 5. Count Plot
# 6. Line Plot

# In[ ]:





# # 1. Scatterplot

# In[43]:


plt.figure(figsize=(15,15))
plt.scatter(x=covid["vaccines"],y=covid["country"])
plt.title("Vaccines in each country")
plt.ylabel("country") # dependent
plt.xlabel("vaccines") # independent 
plt.show()


# # 2. pairplot

# In[45]:


sns.pairplot(covid)
plt.show()
# stuff about what is happenning here with these variables between its  
# goig to give me a whole picture of the dataset with relationship between each other


# # 3. Pie Chart

# In[46]:


covid.head(2)


# In[47]:


covid['people_fully_vaccinated_per_hundred'].value_counts()


# In[48]:


plt.figure(figsize=(10,10))
covid['people_fully_vaccinated_per_hundred'].value_counts().plot.pie(autopct="%1.1f%%",explode=(0,0.2,0,0,0,0,0,0,0,0,0,0,0,0),)
plt.title("people_fully_vaccinated_per_hundred count with percentage")
plt.show()
# explot will help us to highlight a particular category pie


# # 4. Histogram (Distplot)

# In[49]:


covid.head(2)


# In[50]:


total_vaccinations_mean=covid["total_vaccinations"].mean()
total_vaccinations_median=covid["total_vaccinations"].median()


# In[51]:


plt.figure(figsize=(8,8))
sns.distplot(covid["total_vaccinations"])
# vertical line to understand skewness of data on based of mean and median
plt.axvline(total_vaccinations_mean,color='red')
plt.axvline(total_vaccinations_median,color='yellow')
plt.show()


# help me to understand data ditribution is normal ball curved or skewd 


# In[52]:


# vertical line to understand skewness of data on based of mean and median
# total_vaccinations column data is right side skewd so can see its not normally distributed 


# In[ ]:





# # 5. Count Plot (Barplot in matplotlib)

# In[55]:


covid["vaccines"].value_counts()


# In[56]:


plt.figure(figsize=(10,10))
plt.rcParams['axes.facecolor'] = 'black'
sns.countplot(data=covid,y="vaccines")                                                                 # #horizontal Count plot
plt.show()


# #  6. Line Plot

# In[53]:


covid.head(2)


# In[54]:


x=covid['total_vaccinations']
y=covid['country']
plt.figure(figsize=(10,10))
print("Length of variable x => ",len(x) )
print("Length of variable y => ",len(y))
plt.plot(covid['total_vaccinations'],covid['country'])
plt.title('Vaccination growth in each country')
plt.legend(labels=['Vaccination Rate'])
plt.xlabel('total_vaccinations')
plt.ylabel('country')
plt.plot(x,y,color='black',linewidth=4,marker='o',markersize=8,markeredgecolor='black')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




