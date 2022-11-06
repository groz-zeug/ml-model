import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

# Loading data
data_1 = pd.read_csv('startup_funding2019.csv')
data_2 = pd.read_csv('startup_funding2020.csv')
data_2 = data_2.drop(['Unnamed: 9'], axis = 1)
data_3 = pd.read_csv('startup_funding2021.csv')


# Data Formatting and Cleaning
startups = pd.concat([
    data_1,
    data_2,
    data_3
], ignore_index=True)

startups = startups.drop([
    'Company/Brand',
    'Founders',
    'Founded'
], axis = 1)

startups = startups.dropna(subset=['Amount($)'])

startups = startups[startups['Amount($)'].astype(str).str.replace(r'[$,\,]', '').str.isnumeric()]
startups['Amount(M$)'] = startups['Amount($)'].astype(str).str.replace(',', '').str.replace('$', '').astype(float) / 1000000

# startups.to_csv("cleaned_data.csv")

startups = pd.read_csv('cleaned_data.csv')


# Visualization

# Major Startup Sectors
startups["Sector"] = startups["Sector"].str.lower()
plt.figure(figsize=(16,20))

plt.title("Startups in each sector")
sns.barplot(y= startups['Sector'].value_counts().index[:20],x= startups['Sector'].value_counts().values[:20])
plt.ylabel("Sector")
plt.show()

# Major Startup Locations
plt.figure(figsize=(16,20))

plt.title("Startups ideal locations")
sns.barplot(x= startups['HeadQuarter'].value_counts().index[:20],y= startups['Sector'].value_counts().values[:20])
plt.xlabel("Headquarters")
plt.xticks(rotation = 90)
plt.show()

# Startup sector funded more
startup_funds_per_sector = startups.groupby(["Sector"]).aggregate(func='sum')["Amount(M$)"].sort_values(ascending=False)

plt.figure(figsize=(16,10))
plt.title("Startups funded more")
sns.barplot(y= startup_funds_per_sector.index[:20], x= startup_funds_per_sector.values[:20])
plt.ylabel("Sector")
plt.xlabel("Funding in Million $")
plt.show()

# Prime startup location
startup_funding_per_sector = startups.groupby(["HeadQuarter"]).aggregate(func='mean')["Amount(M$)"].sort_values(ascending=False)

plt.figure(figsize=(16,15))

plt.title("Average funding per start-up in each location")
sns.barplot(y=startup_funding_per_sector.index[:25],x=startup_funding_per_sector.values[:25])
plt.ylabel("HeadQuarter")
plt.xlabel("Funding in Million $")
plt.show()
