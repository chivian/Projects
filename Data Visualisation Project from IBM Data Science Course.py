
# coding: utf-8

# ## Final Project on Data Visualization IBM Course

# In this project we would be looking at some key data vusualization tools and packages in python

# In[1]:


#Import the necessary libraries
import pandas as pd
import numpy as npaA
import matplotlib as mpl
import matplotlib.pyplot as plt
print("Done!")


# Nest we woild import the data we would be using 

# In[2]:


file =  'https://cocl.us/datascience_survey_data'
df = pd.read_csv(file)
df


# ## Task One

# A survey was conducted to gauge an audience interest in different data science topics, namely:
# 
# Big Data (Spark / Hadoop)
# Data Analysis / Statistics
# Data Journalism
# Data Visualization
# Deep Learning
# Machine Learning
# The participants had three options for each topic: Very Interested, Somewhat interested, and Not interested. 2,233 respondents completed the survey
# .
# 
# The survey results have been saved in a csv file and can be accessed through this link: __[Topic_Survey_Assignment]('https://cocl.us/datascience_survey_data')__
# 
# If you examine the csv file, you will find that the first column represents the data science topics and the first row represents the choices for each topic.
# 
# 

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
df.sort_values(by=['Very interested'], inplace=True, ascending=False)
df.rename(columns={'Unnamed: 0':'Topic'},inplace=True)
df_perc = df[['Topic']]
df_perc = df_perc.join((df[['Very interested','Somewhat interested','Not interested']]/2233)*100)
df_perc.set_index('Topic', inplace=True)
df_perc.round(2)


# ## Task Two

# Use the artist layer of Matplotlib to replicate the bar chart below to visualize the percentage of the respondents' interest in the different data science topics surveyed.
# 
# To create this bar chart, you can follow the following steps:
# 
# Sort the dataframe in descending order of Very interested.
# Convert the numbers into percentages of the total number of respondents. Recall that 2,233 respondents completed the survey. Round percentages to 2 decimal places.
# As for the chart:
# use a figure size of (20, 8),
# bar width of 0.8,
# use color #5cb85c for the Very interested bars, color #5bc0de for the Somewhat interested bars, and color #d9534f for the Not interested bars,
# use font size 14 for the bar labels, percentages, and legend,
# use font size 16 for the title, and,
# display the percentages above the bars as shown above, and remove the left, top, and right borders.

# In[4]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

labels =['Data Analysis / Statistics','Machine Learning','Data Visualization','Big Data (Spark / Hadoop)','Deep Learning','Data Journalism']
very_int = df_perc['Very interested']
some_int = df_perc['Somewhat interested']
not_int = df_perc['Not interested']

ind = np.arange(len(very_int))  
width = 0.3

fig, ax = plt.subplots(figsize=(20,8))
rects1 = ax.bar(ind - width, very_int, width, label='Very interested', color='#5cb85c')
rects2 = ax.bar(ind, some_int, width, label='Somewhat interested', color='#5bc0de')
rects3 = ax.bar(ind + width, not_int, width, label='Notr interested', color='#d9534f')

ax.set_title("Percentage of Respondents' Interest In Data Science Areas", fontsize=16)
ax.set_xticks(ind)
ax.set_xticklabels((labels))
ax.get_yaxis().set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(fontsize=14)

def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height().round(2)
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos]*3, 3),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom', fontsize=14)


autolabel(rects1, "center")
autolabel(rects2, "center")
autolabel(rects3, "center")

fig.tight_layout()

plt.show()


# ## Task Three

# In the final lab, we created a map with markers to explore crime rate in San Francisco, California. In this question, you are required to create a Choropleth map to visualize crime in San Francisco.
# 
# Before you are ready to start building the map, let's restructure the data so that it is in the right format for the Choropleth map. Essentially, you will need to create a dataframe that lists each neighborhood in San Francisco along with the corresponding total number of crimes(including all the 39 crime type categories).
# 
# Based on the San Francisco crime dataset, you will find that San Francisco consists of 10 main neighborhoods, namely:
# 
# Central,
# Southern,
# Bayview,
# Mission,
# Park,
# Richmond,
# Ingleside,
# Taraval,
# Northern, and,
# Tenderloin.
# Convert the San Francisco dataset, which you can also find here, __[San Francisco dataset]('https://cocl.us/sanfran_crime_dataset')__, into a pandas dataframe, like the one shown below, that represents the total number of crimes in each neighborhood.
# 
# Paste this link in the browser and download the zip file.
# 
# Extract the csv file from the zip file.
# 
# Later upload the csv file to skills lab and use it.
# 
# 

# In[7]:


file =  'https://cocl.us/sanfran_crime_dataset'
df_sf = pd.read_csv(file)
df_sf.head()


# In[8]:


df_sf_neigh = df_sf.groupby(["PdDistrict"]).count().reset_index()
df_sf_neigh.drop(df_sf_neigh.columns.difference(['PdDistrict','IncidntNum']), 1, inplace=True)
df_sf_neigh.rename(columns={'PdDistrict':'Neighborhood','IncidntNum':'Count'}, inplace=True)
df_sf_neigh


# ## Task Four

# Now you should be ready to proceed with creating the Choropleth map.
# 
# As you learned in the Choropleth maps lab, you will need a GeoJSON file that marks the boundaries of the different neighborhoods in San Francisco. In order to save you the hassle of looking for the right file, I already downloaded it for you and I am making it available via this link: __[GeoJSON]('https://cocl.us/sanfran_geojson')__
# 
# For the map, make sure that:
# 
# it is centred around San Francisco,
# you use a zoom level of 12,
# you use fill_color = 'YlOrRd',
# you define fill_opacity = 0.7,
# you define line_opacity=0.2, and,
# you define a legend and use the default threshold scale.
# If you follow the lab on Choropleth maps and use the GeoJSON correctly, you should be able to generate the following map:

# In[9]:


get_ipython().system('wget --quiet https://cocl.us/sanfran_geojson')
get_ipython().system('conda install -c conda-forge folium=0.5.0 --yes')
import folium

print('Folium installed and imported!')
print('GeoJSON file downloaded!')


# In[12]:


sf_geo = 'https://cocl.us/sanfran_geojson'

sf_latitude = 37.77
sf_longitude = -122.42
sf_map = folium.Map(location=[sf_latitude,sf_longitude], zoom_start=12)


# In[11]:


sf_map.choropleth(
    geo_data=sf_geo,
    data=df_sf_neigh,
    columns=['Neighborhood', 'Count'],
    key_on='feature.properties.DISTRICT',
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Crime Rate per District in San Francisco')

sf_map

