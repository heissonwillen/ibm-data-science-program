import pandas as pd
import folium
from folium import plugins

import os
import webbrowser

def display_map(map):
	map_path = str(os.getcwd()+'/map.html')
	map.save(map_path)
	webbrowser.open('file://'+map_path)

'''
world_map = folium.Map(
	location=[56.130, -106.35], 
	zoom_start=2,
	tiles='Stamen Terrain'
	)
'''

df_incidents = pd.read_csv('Police_Department_Incidents.csv')
limit = 100
df_incidents = df_incidents.iloc[0:limit, :]

latitude = 37.77
longitude = -122.42

sanfran_map = folium.Map(
	location=[latitude, longitude], 
	zoom_start=12
	)

incidents = folium.map.FeatureGroup()

'''
for lat, lng in zip(df_incidents.Y, df_incidents.X):
	incidents.add_child(
		folium.features.CircleMarker(
			[lat, lng],
			radius=5,
			color='yellow',
			fill=True,
			fill_color='blue',
			fill_opacity=0.6
			)
		)
'''

latitudes = list(df_incidents.Y)
longitudes = list(df_incidents.X)
labels = list(df_incidents.Category)

'''
for lat, lng, label in zip(latitudes, longitudes, labels):
	folium.Marker(
		[lat, lng], 
		popup=label
		).add_to(sanfran_map)

sanfran_map.add_child(incidents)
'''

incidents = plugins.MarkerCluster().add_to(sanfran_map)

for lat, lng, label in zip(latitudes, longitudes, labels):
	folium.Marker(
		location=[lat,lng],
		icon=None,
		popup=label,
		).add_to(incidents)

display_map(sanfran_map)