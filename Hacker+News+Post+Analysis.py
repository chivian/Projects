#!/usr/bin/env python
# coding: utf-8

# ### Hacker News Data Analysis

# For this project, we are going to doing some analysis on posts and data from the Hacker News website. Hacker News is a technology site thatt features posts that with tech realed contents that get posted based on comments and upvote counts. See this link for more on the website
# [link](https://thehackernews.com/)
# 

# Posts on the Hacker News website are usually classified into two groups, AskHN and Show HN. For this project we are going to try to answer and retrieve the following information:
# * Do Ask HN or Show HN retrieve more comments on the average
# * Do posts created at a certan time recieve ore comments on average?

# #### 1. Importing the libraries and readng the data set into a list of lists

# In[2]:


from csv import reader
opened_file = open('hacker_news.csv')
read_file = reader(opened_file)
hn = list(read_file)
hn[0:5] 


# In[3]:


headers = hn[0]
headers


# In[4]:


hn = hn[1:]
hn[1:6]


# #### 2. Filter through the data to seperate posts beginning with Ask HN and Show HN

# In[5]:


ask_posts = []
show_posts = []
other_posts = []

for row in hn:
    title = row[1]
    if title.lower().startswith('ask hn'):
        ask_posts.append(row)
    elif title.lower().startswith('show hn'):
        show_posts.append(row)
    else:
        other_posts.append(title)

print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))        
    
        
        


# Now let us determine which posts recieve more comments on average

# In[6]:


total_ask_comments = 0
for row in ask_posts:
    num_comments = row[4]
    total_ask_comments += int(num_comments)
    
avg_ask_comments = total_ask_comments/len(ask_posts)
print(avg_ask_comments)

total_show_comments = 0

for row in show_posts:
    num_comments2 = row[4]
    total_show_comments += int(num_comments2)
    
avg_show_comments = total_show_comments/len(show_posts)
print(avg_show_comments)
    


# Now that we have establlished that the 'ask posts' have more comments on the average, we would concentrate our next few analysis on them. Next we would try to determine any relationship between the time these 'ask posts' are created, and the number of comments generated.

# We are going to do this in two stages. First, we would:
# 1. Calculate the number of posts created in each hour of the day with the correxponding number of comments
# 2. Calculate the average number of askposts recieved per hour created.

# #### 1. Number of ask posts and corresponing number of comments per hour

# In[ ]:


import datetime as dt

result_list = [] #this will be a list of lists
for row in ask_posts:
    result_list.append([row[6], int(row[4])])
    
comments_by_hour = {}
counts_by_hour = {}
date_format = "%m/%d/%Y %H:%M"

for row in result_list:
    date = row[0]
    comment = row[1]
    time = dt.datetime.strptime(date, date_format).strftime("%H")
    if time in counts_by_hour:
        comments_by_hour[time] += comment
        counts_by_hour[time] += 1
    else:
        comments_by_hour[time] = comment
        counts_by_hour[time] = 1

comments_by_hour
counts_by_hour

    


# Now that we have created two dictionaries, one with the number of ask posts per hour while the other is the number of comments of these posts each hour. Next, we would use these two data and calculate the average number of comments per post each hour. 
# 

# #### 2. Calculate the average comments for each post for each hour.

# In[10]:


avg_by_hour = []

avg_by_hour = []

for hr in comments_by_hour:
    avg_by_hour.append([hr, comments_by_hour[hr] / counts_by_hour[hr]])

avg_by_hour


# From the output above we can see that it is difficult the see the times with more comments. It would be a great idea to sort the list.

# In[12]:


swap_avg_by_hour = []
for row in avg_by_hour:
    swap_avg_by_hour.append([row[1], row[0]])

print(swap_avg_by_hour)

sorted_swap = sorted(swap_avg_by_hour, reverse=True)

sorted_swap
    


# In[13]:


print("Top 5 Hours for 'Ask HN' Comments")
for avg, hr in sorted_swap[:5]:
    print(
        "{}: {:.2f} average comments per post".format(
            dt.datetime.strptime(hr, "%H").strftime("%H:%M"),avg
        )
    )


# The hour that receives the most comments per post on average is 15:00, with an average of 38.59 comments per post. There's about a 60% increase in the number of comments between the hours with the highest and second highest average number of comments.
# 
# According to the data set documentation, the timezone used is Eastern Time in the US. So, we could also write 15:00 as 3:00 pm est.
# 
# 

# ### Conclusion
# 
# From our analysis we can say that posts that generate more engagements in terms of comments are usually those posted by around 15:00 or 3pm EST. 

# In[ ]:




