import requests

api_key = '8e95a1e4-6d07-488c-8f23-d95874da0c18'  
endpoint = 'https://graphhopper.com/api/1/geocode'
    
location = 'Pashupatinath Mandir kathmandu'    
params = {
  'q': location,
  'key': api_key,
}

response = requests.get(endpoint, params=params)
json_data = response.json()

for i in range(0, len(json_data)):
  name = json_data['hits'][i]['name']
  lat_lng = json_data['hits'][i]['point']
  print(f"{name}--->{lat_lng}")















'''

{'hits': 
[
  {'point': 
    {
    'lat': 28.19826115, 'lng': 84.00222634550191
    }, 
    'extent': [84.0021924, 28.1982425, 84.0022614, 28.19828], 
    'name': 'Shree Rudreshwar Pashupatinath Mandir', 
    'country': 'Nepal', 
    'countrycode': 'NP', 
    'city': 'पोखरा', 
    'state': 'गण्डकी प्रदेश', 
    'street': 'Kajipokhari', 
    'postcode': '33709', 
    'osm_id': 1165593087, '
    osm_type': 'W', 
    'osm_key': 'amenity', 
    'osm_value': 'place_of_worship'}, 

  {'point': 
  {'lat': 27.1779068, 'lng': 84.9767986},
    'name': 'Pashupatinath Mandir Simara', 
    'country': 'Nepal', 
    'countrycode': 'NP', 
    'city': 'Simara', 
    'state': 'मधेश प्रदेश', 
    'street': 'Tribhuban Highway', 
    'postcode': '44417', 
    'osm_id': 9802085600, 
    'osm_type': 'N', 
    'osm_key': 'amenity', 
    'osm_value': 'place_of_worship'}, 
    
  {'point': 
  {'lat': 28.0492916, 'lng': 81.6210278}, 
  'name': 'Shri Pashupatinath Mandir', 
  'country': 'Nepal', 
  'countrycode': 'NP', 
  'city': 'नेपालगन्ज', 
  'state': 'लुम्बिनी प्रदेश', 
  'street': 'Mari Mata Road', 
  'postcode': '21900', 
  'osm_id': 5405165103, 
  'osm_type': 'N', 
  'osm_key': 'amenity', 
  'osm_value': 'place_of_worship'}, 
  
{'point': {'lat': 27.594215, 'lng': 85.4642569}, 
'name': 'पशुपतिनाथ मन्दिर', 
'country': 'Nepal', 
'countrycode': 'NP', 
'city': 'Chundunga', 
'state': 'बाग्मती प्रदेश', 
'street': 'Way to Ashapuri', 
'osm_id': 4373464299, 
'osm_type': 'N', 
'osm_key': 'amenity', 
'osm_value': 'place_of_worship'}], 
'locale': 
'default'}

'''