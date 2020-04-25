import numpy as np
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

def create_waffle_chart(categories, values, height, width, colormap, value_sign=''):
	total_values = sum(values)
	category_proportions = [(float(value) / total_values) for value in df_dsn['Total']]

	'''
	for i, proportion in enumerate(category_proportions):
		print (df_dsn.index.values[i] + ': ' + str(proportion))
	'''

	total_num_tiles = width*height
	tile_per_category = [round(proportion*total_num_tiles) for proportion in category_proportions]

	'''
	for i, tiles in enumerate(tile_per_category):
		print(df_dsn.index.values[i] + ': ' + str(tiles))
	'''

	waffle_chart = np.zeros((height, width))

	category_index = 0
	tile_index = 0

	for col in range(width):
		for row in range(height):
			tile_index += 1

			if tile_index > sum(tile_per_category[0:category_index]):
				category_index += 1

			waffle_chart[row, col] = category_index

	# fig = plt.figure()

	plt.matshow(waffle_chart, cmap=colormap)
	plt.colorbar()

	ax = plt.gca()

	ax.set_xticks(np.arange(-.5, (width), 1), minor=True)
	ax.set_yticks(np.arange(-.5, (height), 1), minor=True)
	    
	ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

	plt.xticks([])
	plt.yticks([])

	values_cumsum = np.cumsum(df_dsn['Total'])
	total_values = values_cumsum[len(values_cumsum)-1]

	legend_handles = []

	for i, category in enumerate(df_dsn.index.values):
		label_str = category + '(' +str(df_dsn['Total'][i]) + ')'
		color_val = colormap(float(values_cumsum[i])/total_values)
		legend_handles.append(mpatches.Patch(color=color_val, label=label_str))

	plt.legend(
		handles=legend_handles,
		loc='lower center',
		ncol=len(df_dsn.index.values),
		bbox_to_anchor=(0., -0.2, 0.95, .1)
		)

	plt.show()


'''
width = 50
height = 50
categories = df_dsn.index.values
values = df_dsn['Total']
colormap = plt.cm.coolwarm

create_waffle_chart(categories, values, height, width, colormap)
'''