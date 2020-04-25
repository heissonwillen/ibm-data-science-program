import numpy as np
import pandas as pd 
import PIL as Image

import matplotlib as mpl 
import matplotlib.pyplot as plt 
# import matplotlib.patches as mpatches

import seaborn as sns

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

# mpl.style.use('ggplot')
# df_dsn = df_can.loc[['Denmark', 'Norway', 'Sweden'], :]

df_tot = pd.DataFrame(df_can[years].sum(axis=0))
df_tot.index = map(float, df_tot.index)
df_tot.reset_index(inplace=True)
df_tot.columns = ['year', 'total']

plt.figure(figsize=(25,10))
sns.set(font_scale=1.5)
sns.set_style('ticks')

ax = sns.regplot(
	x='year',
	y='total',
	data=df_tot,
	color='green',
	marker='+'
	)

ax.set(
	xlabel='Year',
	ylabel='Total immigration',
	)

ax.set_title('Total immigration to Canada from 1980 - 2013')


plt.show()