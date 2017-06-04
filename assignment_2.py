import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("database.csv") # loading the dataset

# Query 1. Plot of 4 weapons with their yearly usage.

#Grouping by year and weapon and finding number of occurences
weapon_year =df['Year'].groupby(df["Weapon"]).value_counts()

#Choosing any 4 weapons
blunt = weapon_year['Blunt Object']
firearm = weapon_year['Firearm']
shotgun = weapon_year['Shotgun']
knife = weapon_year['Knife']

#Plotting them with proper labels

blunt.plot(kind='line',label='Blunt',legend=True)
firearm.plot(kind='line',label='Firearm',legend=True)
shotgun.plot(kind='line',label='Shotgun',legend=True)
knife.plot(kind='line',label='Knife',legend=True)
plt.show()

# Query 2. Plot of 4 Realtionships and year

relationship_year =df['Year'].groupby(df["Relationship"]).value_counts()

husband = relationship_year['Husband']
boyfriend = relationship_year['Boyfriend']
acquaintance = relationship_year['Acquaintance']
stranger = relationship_year['Stranger']

husband.plot(kind='line',label='Husband',legend=True)
boyfriend.plot(kind='line',label='Boyfriend',legend=True)
acquaintance.plot(kind='line',label='acquaintance',legend=True)
stranger.plot(kind='line',label='stranger',legend=True)

plt.show()

# Query 3
# A boxplot of year and weapon that helps see both categorical
# variable's relation at a glace

sns.boxplot(x=df['Year'],y=df['Weapon'])
plt.show()


