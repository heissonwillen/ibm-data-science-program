import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt 

df_can = pd.read_excel(
	'Canada.xlsx',
	sheet_name='Canada by Citizenship',
	skiprows=range(20),
	skipfooter=2
	)

df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis = 1, inplace = True)
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'Regname':'Region'}, inplace=True)
df_can.columns = list(map(str, df_can.columns))
df_can.set_index('Country', inplace=True)
df_can['Total'] = df_can.sum(axis=1)

years = list(map(str, range(1980, 2014)))

df_continents = df_can.groupby('Continent', axis=0).sum()

'''
print(type(df_can.groupby('Continent', axis=0)))
print(df_continents.head())
'''

'''
colors_list = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
explode_list = [0.1, 0, 0, 0, 0.1, 0.1]

df_continents['Total'].plot(
	kind='pie',
	figsize=(5,6),
	autopct='%1.1f%%',
	startangle=90,
	shadow=True,
	labels=None,
	pctdistance=1.12,
	colors=colors_list,
	explode=explode_list
	)

plt.title('Immigration to Canada by Continent [1980 - 2013]')
plt.axis('equal')
plt.legend(labels=df_continents.index, loc='uper left')
plt.show()
'''

'''
df_japan = df_can.loc[['Japan'], years].transpose()
df_japan.plot(kind='box', figsize=(8, 6))

plt.title('Box plot of Japanese Immigrants from 1980 - 2013')
plt.ylabel('Number of Immigrants')
plt.show()
'''

df_CI = df_can.loc[['China', 'India'], years].transpose()

'''
df_CI.plot(kind='box', figsize=(8, 6))
plt.title('Box plot of Indian and Chinese Immigrants from 1980 - 2013')
plt.ylabel('Number of Immigrants')
plt.show()
'''

df_CI.plot(kind='box', figsize=(10, 7), color='blue', vert=False)
plt.title('Box plots of Immigrants from China and India (1980 - 2013)')
plt.xlabel('Number of Immigrants')
plt.show()

# LAST SESSION VIEWED: SUBPLOTS