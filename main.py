import requests
import pandas as pd
import os 

if __name__ == "__main__":
	api_key = os.getenv('WEATHER_API_KEY')

	locations = ['-16.5403795,-68.059136', 'uk', 'us', 'fr', 'ger']
	rows = []

	for loc in locations:
		url = f'https://api.weatherapi.com/v1/current.json?q={loc}&lang=en&key={api_key}'
		response = requests.get(url, timeout=10)
		if response.status_code == 200:
			data = response.json()
			dt_loc = data['location']
			current = data['current']
			rows.append({
				'name': dt_loc['name'],
				'lat': dt_loc['lat'],
				'lon': dt_loc['lon'],
				'last_updated': current['last_updated'],
				'temp_c': current['temp_c'],
				'wind_kph': current['wind_kph'],
				'wind_degree': current['wind_degree'],
				'humidity': current['humidity']
			})

	df = pd.DataFrame(rows)
	save_dir ='data'
	os.makedirs(save_dir,exist_ok=True )
	df.to_csv(os.path.join(save_dir, 'clima.csv'), index=False)