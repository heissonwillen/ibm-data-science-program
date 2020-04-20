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

'''
print('Data read into a pandas dataframe!')
print(df_can.tail())
print(df_can.info())
print(df_can.columns.values)
print(df_can.index.values)
print(type(df_can.columns))
print(type(df_can.index))
print (type(df_can.columns.tolist()))
print (type(df_can.index.tolist()))
print(df_can.shape)

'''
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_can['Total'] = df_can.sum(axis=1)
df_can.isnull().sum()

'''
df_can.Country
df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]]
'''

df_can.set_index('Country', inplace=True)
df_can.index.name = None

'''
print(df_can.loc['Japan'])
print(df_can.iloc[87])
print(df_can[df_can.index == 'Japan'].T.squeeze())

print(df_can.loc['Japan', 2013])
print(df_can.iloc[87, 36])

print(df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]])
print(df_can.iloc[87, [3, 4, 5, 6, 7, 8]])
'''

df_can.columns = list(map(str, df_can.columns))
years = list(map(str, range(1980, 2014)))

condition = df_can['Continent'] == 'Asia'
df_can[condition]
df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]

'''
print('data dimensions: ', df_can.shape)
print(df_can.columns)
'''

'''
print('matplotlib version: ', mpl.__version__)
print(plt.style.available)
'''

'''
mpl.style.use(['ggplot'])

haiti = df_can.loc['Haiti', years]
haiti.index = haiti.index.map(int)
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.text(2000, 6000, '2010 Earthquake')
'''

'''
df_CI = df_can.loc[['India', 'China'], years]
df_CI = df_CI.transpose()
df_CI.index = df_CI.index.map(int)
df_CI.plot(kind='line')

plt.title('Immigration from China and India')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show()
'''

df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
df_top = df_can.head(5)
df_top = df_top[years].transpose()

df_top.index = df_top.index.map(int)
df_top.plot(kind='line', figsize=(14,8))

plt.title('Immigration trend of top fize contries')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show()