# -*- coding: utf-8 -*-
"""QDAA-Tutorial-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/162N4tXzAtYrkTqSZCexzJwK9orfb7gqj

<h1>Importing Libraries</h1>
<p>The first thing we want to do is import our libraries. Libraries are additional pieces of code (code someone else wrote that we are recycling) that can provide a lot of utility that doesn't come with Python out of the box. For pur data
"""

import pandas as pd

"""<h1>Importing Data</h1>
<p>Today we will be using a shopping trends dataset.<p>
<p>The dataset can be viewed on <a href="https://docs.google.com/spreadsheets/d/1cWEVkF8CnkpjdsDRCMSt5e0JkW-SmPjJdb100_wnSGs/edit?usp=sharing">Google Sheets</a>,
<a href="https://github.com/aclarke500/QDAA-tutorials/blob/main/datasets/montreal-airbnb-listings.csv">Github</a>,and downloaded on by clicking <a href="http://data.insideairbnb.com/canada/qc/montreal/2023-10-08/visualisations/listings.csv">here</a> (was sourced <a href="http://insideairbnb.com/get-the-data/">here</a>).<br>
<p>It is always useful to look at the data you are going to be analyzing before running any code with it, so I would encourage you to visually expect this. </p>
<p>
 There are many different ways to import data into Python. In the following code, we import it from Github. If you try and do this, make sure you click the "raw" button on the csv file to get the correct link.</p>
"""

url = "https://raw.githubusercontent.com/aclarke500/QDAA-tutorials/main/datasets/montreal-airbnb-listings.csv"
df = pd.read_csv(url)

"""<h1>Analysing Columns
<p>When analyzing a data set, it's important to see what variables we are working with.
<p>Further, in pandas, dataframes are indexed using strings, similair to Python dictionaries.
<p>Let's print out all the variables so we know both <i>what</i> we are working with and <i>how</i> to index them.
"""

for variable_name in df.columns:
  print(variable_name)

"""<h1>Plotting!</h1>
<p>Now that we know what our variables are and how we can index them, lets plot a histogram and see what we can draw from that.
<p>In order to plot the histogram we're going to use a library called matplot. Matplot is a fantastic tool that makes plotting decent looking graphs very easy.
<p>For starters, we're gonna be plotting a histogram to see how our data is distributed.
"""

# firstly, import matplot
import matplotlib.pyplot as plt

plt.hist(df["price"].tolist(), bins=20, range=(0, 1000),color='#ccd177', edgecolor='black')

# Add titles and labels to make graph look dope af on da gram
plt.title("Prices of Airbnb's in Montréal")
plt.xlabel('$ Per Night')
plt.ylabel('Frequency')

# Plot that thing
plt.show()

"""<h1>Subsetting and Logical Arrays
<p>Often times when working with data, you don't want to look at every piece of data. For instance, you might want to <b>remove outliers</b> or only examine data that match particular <b>properties of interest</b>.
<p>Say, for instance, we are writing an article on budget friendly airbnb's in Montreal. We don't want to examine every single entry, just the cheaper ones.
<p> The way we solve this problem is with a <b>logical array</b>.
<p> Logical arrays are ordered arrays of True and False values that represent which positions are valid and invalid. For instance, if I had a list of things [present, apples, bananas, dogs, oranges], a logical array representing which of those are fruit would be [False, True, True, False, True]. This is useful for telling pandas (or any data analysis tool) which elements we want to consider.

<h2>Implementation!</h2>
Now, we're gonna only grab the places that are less than 150 per night, and create a new dataframe with our cheaper options.
"""

# create list to represent our logical array
indices_of_cheap_airbnb = df['price'] <= 100

# hold our "cheap" airbnbs in a new dataframe
cheap_df = df[indices_of_cheap_airbnb]
cheap_df.head() # you can just call variables and they print

"""<h2>Subsetting by Columns</h2>
<p>Another way we can subset dataframes is by grabbing certain columns we want, to make the dataframe less bloated
"""

cheap_df = cheap_df[['price', 'latitude', 'longitude', 'minimum_nights']]

cheap_df.head()

"""<h2>Examine</h2>
<p>Now lets see <b>where</b> these hotels are!
"""

cheap_latitude = cheap_df['latitude'].tolist()
cheap_longitude = cheap_df['longitude'].tolist()

plt.scatter( cheap_latitude, cheap_longitude, c='#77d18f')

plt.title("Heatmap of Cheap Airbnbs in Montreal")
plt.ylabel('Longitude')
plt.xlabel('Latitude')

plt.show()

"""<h1>Challenge!</h1>
<p>I'm going to Montreal with my favourite QDAA members (including you if you help me out here) after exam season is over. <p>I want a decently priced, but not too cheap, airbnb between $100-200 (inclusive).
<p>However, since we have to head back for the holidays, we can only stay for a few days, so the minimum number of nights must be less than or equal to 2. Give me the list of hotels in this price range.

<b>Requirements</b>
<ul>
<li>Less than 200 dollars</li>
<li> More than 100 dollars</li>
<li>Minimum Stay is at most 2 nights
<ul>
<p>Once you get them, plot some of your favourite variables against eachother</p>
"""

import pandas as pd

url = "https://raw.githubusercontent.com/aclarke500/QDAA-tutorials/main/datasets/montreal-airbnb-listings.csv"
df = pd.read_csv(url)

import matplotlib.pyplot as plt

# indices_of_cheap_airbnb = df['price'] < 200
# cheap_price = df[indices_of_cheap_airbnb]
# new_indicies_of_cheap = cheap_price["price"] >100
# new_cheap_price = df[new_indicies_of_cheap]

cheap_prices = (df['price'] < 200) & (df['price'] > 100) & (df['minimum_nights']< 3).tolist()
cheap_prices.head()
cheap_df = df[cheap_prices]
plt.hist(cheap_df["price"], bins=20)
plt.show()

cheap_df = df[cheap_prices]
cheap_df.head()



"""<h1>Bonus challenge!</h1>
<ul>
<li>Must be less than 0.1 units on the longitude latitude board from my favourite poutine place, <i>Poutineville Bishop</i> located at 45.495880, -73.575490.
<ul>

"""

poutine_spot=(45.495880, -73.575490) # location of poutinery
theta = 0.01 # maximum acceptable distance

"""<h2>Hints!</h2>
<p>In order to get the distance between two points, you can use the formula $d = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$

<h2>Plot Solution</h2>
"""

fig, ax = plt.subplots()
ax.scatter(cheap_df['latitude'], cheap_df['longitude'], c='#77d18f', label='Close to Poutine Bishop') # replace with or add solution dataframe
ax.scatter(poutine_spot[0], poutine_spot[1], c='blue', marker='h', label='Poutine Bishop')

# plot circle
circle = plt.Circle(poutine_spot, theta, fill=False, color='red', linewidth=2, label='Radius around Poutine Bishop')
ax.add_artist(circle)
# Add labels and legend
ax.set_xlabel('longitude')
ax.set_ylabel('latitude')
ax.set_title("Highlighting Spots Close to Adam's Fave Poutine Spot")
ax.legend()


ax.set_xlim([45.45, 45.52])  # Set X-axis limits
ax.set_ylim([-73.6, -73.5])  # Set Y-axis limits
ax.set_aspect('equal')  # Ensure the aspect ratio is equal

# Display the plot with grid
plt.grid(True)
plt.show()