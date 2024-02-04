import requests

api_key = '8e95a1e4-6d07-488c-8f23-d95874da0c18'  
endpoint = 'https://graphhopper.com/api/1/geocode'

# Provide latitude and longitude for reverse geocoding
latitude = 27.7083895
longitude = 85.3443544

params = {
    'point': f'{latitude},{longitude}',
    'reverse': 'true',
    'key': api_key,
}

response = requests.get(endpoint, params=params)
json_data = response.json()

# Check if the response has hits
if 'hits' in json_data:
    for hit in json_data['hits']:
        name = hit.get('name', 'Unknown')
        lat_lng = hit.get('point', {})
        print(f"{name} ---> {lat_lng}")
else:
    print("No hits found in the reverse geocoding response.")

























