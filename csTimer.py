#!/usr/bin/env python
# coding: utf-8

# In[60]:


import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import os
from datetime import datetime
import json


# In[61]:


downloadlist = os.listdir("/Users/kaust/Downloads")
cstimerfiles = []
for x in downloadlist:
    if x.startswith('cstimer'):
        cstimerfiles.append(x)
statsfile = max(cstimerfiles)
path = "/Users/kaust/Downloads/" + statsfile


# In[62]:


j = open(path,'r')                                              # Opens the text file with the stats
jj = j.read()
stats = json.loads(jj)                                          # Converts the string to JSON to Dictionary
num_of_tries = len(stats['session1'])                           # Empty Lists for times and dates
dates = []
times = []
ao12_averages = []
ao5_averages = []
for i in range(num_of_tries):                                   # For each solve recorded,
    temp = stats['session1'][i][0][1]//10
    times.append(temp/100)
    if i >= 5:
        val = (sum(times[i-5:i]) - min(times[i-5:i]) - max(times[i-5:i]))/3
        ao5_averages.append(round(val,2))
    if i >= 12:
        val = (sum(times[i-12:i]) - min(times[i-12:i]) - max(times[i-12:i]))/10
        ao12_averages.append(round(val,2))                                        # Add it to the times list
        


# In[63]:


x = np.arange(0, num_of_tries, 1)                               # Take solves on X Axis
y = np.array(times)                                             # Make the times list as NumPy Array
fig, ax = plt.subplots(figsize=(24,6))

#ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))  # Add a 2 decimal place to Y Axis
plt.gca().set_ylim([20,90])                                 # Limiting the Y Axis values
plt.xticks(np.arange(0, num_of_tries, 5))                          # Ranging the values on Y Axis at levels of 0.30
#ax.set_yticklabels(['0','10'])
plt.gca().invert_yaxis()                                        # Invert values so 0 is on top of axis

plt.xlabel("Number of Tries")
plt.ylabel("Time taken")
ax.set_title('Every Solve',fontdict={'fontsize': 20})
ax.plot(x, y)                                                   # Plot values
labels = []
for xs,ys in zip(x,y):                                          # Ripped off code to print values at each point
    label = "{:.2f}".format(ys)
    labels.append(label)
    if len(labels) > 2:
        if labels[-2] < label:
            label = " "
    plt.annotate(label, # this is the text
                 (xs,ys), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center')
plt.show()                                                      # Show

# ---------------------------------------AO5-----------------------------------------------------------------

x = np.arange(5, num_of_tries, 1)                               # Take solves on X Axis
y = np.array(ao5_averages)                                      # Make the times list as NumPy Array
fig, ax = plt.subplots(figsize=(24,6))

#ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))  # Add a 2 decimal place to Y Axis
plt.gca().set_ylim([45,80])                                 # Limiting the Y Axis values
plt.xticks(np.arange(0, num_of_tries, 5))                          # Ranging the values on Y Axis at levels of 0.30
plt.gca().invert_yaxis()                                        # Invert values so 0 is on top of axis

plt.xlabel("AO12")
plt.ylabel("Time taken")

ax.plot(x, y)                                                   # Plot values
ax.set_title('Avg of 5',fontdict={'fontsize': 20})
labels = []
for xs,ys in zip(x,y):                                          # Ripped off code to print values at each point
    label = "{:.2f}".format(ys)
    labels.append(label)
    if len(labels) > 5:
        if min(labels[len(labels)-5:]) < label:
            label = " "
    if len(labels) > 2 and label != " ":
        if abs(float(label) - float(labels[-2])) < 1:
            text = (0,-20)
        else:
            text = (0,10)
    plt.annotate(label, # this is the text
                 (xs,ys), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=text, # distance from text to points (x,y)
                 ha='center')
plt.show()

# ---------------------------------------AO12-----------------------------------------------------------------

x = np.arange(12, num_of_tries, 1)                               # Take solves on X Axis
y = np.array(ao12_averages)                                      # Make the times list as NumPy Array
fig, ax = plt.subplots(figsize=(24,6))

#ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))  # Add a 2 decimal place to Y Axis
plt.gca().set_ylim([50,80])                                 # Limiting the Y Axis values
plt.xticks(np.arange(0, num_of_tries, 5))                          # Ranging the values on Y Axis at levels of 0.30
plt.gca().invert_yaxis()                                        # Invert values so 0 is on top of axis

plt.xlabel("AO12")
plt.ylabel("Time taken")

ax.plot(x, y)                                                   # Plot values
ax.set_title('Avg of 12',fontdict={'fontsize': 20})
labels = []
for xs,ys in zip(x,y):                                          # Ripped off code to print values at each point
    label = "{:.2f}".format(ys)
    labels.append(label)
    if min(labels) < label:
        label = " "
    if len(labels) > 2 and label != " ":
        if abs(float(label) - float(labels[-2])) < 1:
            text = (0,-20)
        else:
            text = (0,10)
    plt.annotate(label, # this is the text
                 (xs,ys), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=text, # distance from text to points (x,y)
                 ha='center')
plt.show()


# In[ ]:





# In[ ]:




