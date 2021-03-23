import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize


years = ['1992','1996','2000','2004','2008','2012','2016']
#Lithuanian data
df = pd.read_csv('LT_data.csv')
df = df[years]
df = df[-1:]

#Latvian data
df2 = pd.read_csv('LV_data.csv')
df2 = df2[years]

df = df.apply(pd.to_numeric, errors = 'coerce')
df2 = df2.apply(pd.to_numeric, errors = 'coerce')
df2.loc['total']= df2.sum(numeric_only = True, skipna=True)
df2 = df2[-1:]

df.reset_index(inplace=True)

df2 = df2.T
df2.reset_index(inplace=True)
df = df.rename(columns={'index': 'Year', 18:'partic_count'})
df2 = df2.rename(columns={'index': 'Year', 'total':'partic_count2'})

df3 = df.join(df2['partic_count2'])

plt.figure()
plt.plot(df3['Year'], df3['partic_count'], '-o', label = "Lithuania", alpha=0.5)
plt.plot(df3['Year'], df3['partic_count2'], '-o', label = "Latvia")
plt.xlabel('Year')
plt.ylabel('Count of participants')
plt.title('Comparison of Olympic games participants count from LT and LV after 1990')
plt.legend()

plt.show()
