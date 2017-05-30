# assignment 1
# query 1- Number of crimes solved

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("database.csv")
unsolved = df[df["Perpetrator Sex"]=="Unknown"]

solved = len(df) - len(unsolved)

# query 2 - Top 5 weapons used

df_weapon = df.groupby(by="Weapon").sum()
df_weapon_max = df_weapon.sort_values("Perpetrator Count",ascending=False)

'''Handgun                 62892  
Blunt Object               13064  
Knife                      12782  
Firearm                    10370  
Shotgun                    5551 '''



# query 3 top weapon each state with its percentage

s = df['Weapon'].groupby(df["State"]).value_counts()
f = s.groupby(level=0).nlargest(1)

su = s.groupby(level=0).sum()
l = list(su.values)

for i in range(len(l)):
    print(f[i:(i+1)]/l[i])

# query 4 bar plot with year

df_year = df.groupby("Year")  
xaxis =list(df_year.groups.keys()) 

#setting ticks to rotate

fig,ax = plt.subplots()
for labels in ax.xaxis.get_ticklabels():
	labels.set_rotation(45)

sns.barplot(x=xaxis,y=df_year.size())
plt.show()




