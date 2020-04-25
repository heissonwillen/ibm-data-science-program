import pandas as pd
import numpy as np
import folium
from folium import plugins
import json

import os
import webbrowser

def display_map(map):
	map_path = str(os.getcwd()+'/map.html')
	map.save(map_path)
	webbrowser.open('file://'+map_path)

df_can = pd.read_excel(
	'Canada.xlsx',
	sheet_name='Canada by Citizenship',
	skiprows=range(20),
	skipfooter=2
	)

df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace=True)
df_can.columns = list(map(str, df_can.columns))
df_can['Total'] = df_can.sum(axis=1)

years = list(map(str, range(1980, 2014)))

world_geo = r'world_countries.json'

world_map = folium.Map(
	location=[0,0],
	zoom_start=2,
	tiles='Mapbox Bright'
	)

threshold_scale = np.linspace(
	df_can['Total'].min(),
	df_can['Total'].max(),
	6,
	dtype=int
	)

threshold_scale = threshold_scale.tolist()
threshold_scale[-1] += 1

world_map.choropleth(
    geo_data=world_geo,
    data=df_can,
    columns=['Country', 'Total'],
    key_on='feature.properties.name',
    threshold_scale=threshold_scale,
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Immigration to Canada',
    reset=True
)

display_map(world_map)