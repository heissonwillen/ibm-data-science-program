import numpy as pn
import pandas as pd 
import PIL as Image

import matplotlib as mpl 
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches

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

mpl.style.use('ggplot')

df_dsn = df_can.loc[['Denmark', 'Norway', 'Sweden'], :]

# Step 1: determinating the proportion of each item with respect to the total
total_values = sum(df_dsn['Total'])
category_proportions = [(float(value) / total_values) for value in df_dsn['Total']]

for i, proportion in enumerate(category_proportions):
	print (df_dsn.index.values[i] + ': ' + str(proportion))

# Step 2: defining the overall size of the waffle chart
width = 40
height = 10

total_num_tiles = width*height

# Step 3: using the proportion of each category to determine it respective number of tiles
tile_per_category = [round(proportion*total_num_tiles) for proportion in category_proportions]

for i, tiles in enumerate(tile_per_category):
	print(df_dsn.index.values[i] + ': ' + str(tiles))

waffle_chart = np.zeros((height, width))