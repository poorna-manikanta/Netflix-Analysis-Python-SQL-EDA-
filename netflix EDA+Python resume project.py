 #Import libraries & dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\Admin\Documents\360 digitmg\resume projects\netflix_titles.csv")
print(df.head())
print(df.info())

# Data Cleaning
# Handle null values
df.fillna("Unknown", inplace=True)

# Convert date_added to datetime
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

# Extract year from date_added
df["year_added"] = df["date_added"].dt.year

# Exploratory Data Analysis
#Movies vs TV Shows
sns.countplot(x="type", data=df, palette="Set2")
plt.title("Movies vs TV Shows")
plt.show()

#Content Added per Year
df["year_added"].value_counts().sort_index().plot(kind="bar", figsize=(12,5))
plt.title("Content Added by Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()

#Top 10 Countries
df["country"].value_counts().head(10).plot(kind="bar", color="skyblue")
plt.title("Top 10 Countries with Most Content")
plt.show()

#Rating Distribution
sns.countplot(y="rating", data=df, order=df["rating"].value_counts().index)
plt.title("Ratings Distribution")
plt.show()

#Genre Analysis
from collections import Counter
genres = df["listed_in"].str.split(", ").sum()
pd.Series(Counter(genres)).nlargest(10).plot(kind="bar", color="orange")
plt.title("Top 10 Genres on Netflix")
plt.show()


#Key Python Insights

#Netflix has more Movies than TV Shows

#Peak growth in 2017–2020

#Most content comes from USA, India, UK

#TV-MA & TV-14 are the most common ratings

#Popular genres → International Movies, Dramas, Comedies