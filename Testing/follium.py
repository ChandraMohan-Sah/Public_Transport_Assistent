import folium

# Updated data for locations
locations_data = {
    "my_location_name": "Thapathali Engineering Campus",
    "my_location_lat_long": [27.694567499999998, 85.3189885018991],
    "nearest_user_station_id": 1069,
    "nearest_user_station_english_name": "Thapathali Campus",
    "nearest_user_station_lat_long": [27.6939878, 85.319277],
    "nearest_dest_station_id": 1019,
    "nearest_dest_station_english_name": "Koteshwor Bus Stop B",
    "nearest_dest_station_lat_long": [27.678413631154278, 85.34901302307844],
    "dest_location_name": "Mandala Family Fast Food",
    "dest_location_lat_long": [27.6779234, 85.3471398]
}

# Create a Folium map centered around the first location
map_center = locations_data["my_location_lat_long"]
my_map = folium.Map(location=map_center, zoom_start=14)

# Add markers for each location
folium.Marker(
    location=locations_data["my_location_lat_long"],
    popup=locations_data["my_location_name"],
    icon=folium.Icon(color='green')
).add_to(my_map)

folium.Marker(
    location=locations_data["nearest_user_station_lat_long"],
    popup=locations_data["nearest_user_station_english_name"],
    icon=folium.Icon(color='red')
).add_to(my_map)

folium.Marker(
    location=locations_data["nearest_dest_station_lat_long"],
    popup=locations_data["nearest_dest_station_english_name"],
    icon=folium.Icon(color='red')
).add_to(my_map)

folium.Marker(
    location=locations_data["dest_location_lat_long"],
    popup=locations_data["dest_location_name"],
    icon=folium.Icon(color='green')
).add_to(my_map)

# Save the map to an HTML file or display it
my_map.save("map.html")
