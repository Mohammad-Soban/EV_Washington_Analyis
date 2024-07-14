import folium
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from folium import plugins

longitude = -77.03637
latitude = 38.89511

df = pd.read_csv("./Data/Electric_Vehicle_Population_Data.csv", low_memory=False)
df = df[pd.to_numeric(df['Latitude'], errors='coerce').notnull()]

df.dropna(subset=['Electric Range'], inplace=True)

sf_map = folium.Map(location=[latitude, longitude], zoom_start=8)
car_sold = plugins.MarkerCluster().add_to(sf_map)

for lat, long, label in zip(df.Latitude, df.Longitude, df.County):
    folium.Marker(
        [lat, long],
        fill =True,
        radius = 5,
        fill_color = 'red',
        fill_opacity = 0.7,
        popup= label
    ).add_to(car_sold)

sf_map.save("map.html")