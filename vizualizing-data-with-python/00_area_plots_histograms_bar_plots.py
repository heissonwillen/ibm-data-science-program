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
print('Data downloaded and read into a data frame!')
'''

df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis = 1, inplace = True)
df_can.rename(columns={'OdName':'Country', 'AreadName':'Continent', 'Regname':'Region'}, inplace=True)

df_can.columns = list(map(str, df_can.columns))
df_can.set_index('Country', inplace=True)
df_can['Total'] = df_can.sum(axis=1)

years = list(map(str, range(1980, 2014)))

mpl.style.use('ggplot')

df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True)

df_top_5 = df_can.head()
df_top_5 = df_top_5[years].transpose()

'''
df_top_5.index = df_top_5.index.map(int)
df_top_5.plot(
	alpha=0.25,
	kind='area',
	stacked=False,
	figsize=(20,10)
	)

plt.title('Immigration trend of top 5 Countries')
plt.xlabel('Number of immigrants')
plt.ylabel('years')

plt.show()
'''

'''
ax = df_top_5.plot(
	kind='area',
	alpha=0.5,
	figsize=(20,10)
	)

ax.set_title('Immigration trend of top 5 Countries')
ax.set_ylabel('Number of immigrants')
ax.set_xlabel('Years')
'''

'''
df_least_5 = df_can.tail()
df_least_5 = df_least_5[years].transpose()
df_least_5.index = df_least_5.index.map(int)

df_least_5.plot(
    alpha=0.25,
    kind='area',
    stacked=False,
    figsize=(20,10)
    )

plt.title('Immigration trend of top 5 Countries')
plt.xlabel('Number of immigrants')
plt.ylabel('years')

plt.show()
'''

'''
print(df_can['2013'].head())
print(df_top_5.head())
print(years)
print(df_can.head())
print('data dimensions: ', df_can.shape)
print(all(isinstance(column, str) for column in df_can.columns))
'''

count, bin_edges = np.histogram(df_can['2013'])

'''
print(count)
print(bin_edges)
'''

'''
df_can['2013'].plot(
	kind='hist',
	figsize=(8,5),
	xticks=bin_edges
	)

plt.title('Histogram of immigration from 195 countries in 2013')
plt.xlabel('Number of countries')
plt.ylabel('Number of immigrants')

plt.show()
'''

'''
df_can.loc[['Denmark', 'Norway', 'Sweden'], years].plot.hist()
'''

'''
df_t = df_can.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()
count, bin_edges = np.histogram(df_t, 15)
xmin = bin_edges[0]-10
xmax = bin_edges[-1]+10

df_t.plot(
	kind='hist',
	figsize=(10,6),
	bins=15,
	xticks=bin_edges,
	color=['coral', 'darkslateblue', 'mediumseagreen'],
	xlim=(xmin,xmax)
	)

plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')

plt.show()
'''

'''
for name, hex in mpl.colors.cnames.items():
	print(name, hex)
'''

'''
df_u = df_can.loc[['Greece', 'Albania', 'Bulgaria'], years].transpose()
count, bin_edges = np.histogram(df_u, 15)

xmin = bin_edges[0]-10
xmax = bin_edges[-1]+10

df_u.plot(
	kind='hist',
	figsize=(10,6),
	bins=15,
	alpha=0.35,
	xticks=bin_edges,
	color=['coral', 'darkslateblue', 'mediumseagreen'],
	xlim=(xmin,xmax)
	)

plt.title('Histogram of Immigration from Greece, Albania, and Bulgaria from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')

plt.show()
'''

'''
df_iceland = df_can.loc['Iceland', years]
df_iceland.plot(kind='bar', figsize=(10, 6))

plt.xlabel('Year') 
plt.ylabel('Number of immigrants') 
plt.title('Icelandic immigrants to Canada from 1980 to 2013')

plt.annotate(
	'',
	xy=(32,70),
	xytext=(28,20),
	xycoords='data',
	arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=2)
	)

plt.annotate(
	'2008 - 2011 financial crisis',
	xy=(28,30),
	rotation=72.5,
	va='bottom',
	ha='left'
	)

plt.show()
'''

df_can.sort_values(by='Total', ascending=True, inplace=True)
df_top_15 = df_can.head(15)

df_top_15.plot(kind='barh', figsize=(12, 12), color='steelblue')
plt.xlabel('Number of Immigrants')
plt.title('Top 15 Conuntries Contributing to the Immigration to Canada between 1980 - 2013')

plt.show()