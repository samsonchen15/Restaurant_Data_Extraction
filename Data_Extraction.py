import requests
import pandas as pd
import json

url = "https://raw.githubusercontent.com/Papagoat/brain-assessment/main/restaurant_data.json"
response = requests.get(url) #Connect to url

if response.status_code == 200: #Connection is successful
    data = response.json() #Extract the JSON data
    print("Connection is successful")
else:
    print(f"Connection failed with status code {response.status_code}")
    
restaurants_data = []

print(f"Extracting Restaurants Data...")

for results in data:
    for restaurants in results['restaurants']:
        restaurant_info = restaurants['restaurant']
        
        extracted_info = {
            'Restaurant ID': restaurant_info['R']['res_id'],
            'Restaurant Name': restaurant_info['name'],
            'Country Code': restaurant_info['location']['country_id'],
            'City': restaurant_info['location']['city'],
            'User Rating Votes': restaurant_info['user_rating']['votes'],
            'User Aggregate Rating': float(restaurant_info['user_rating']['aggregate_rating']),
            'Cuisines': restaurant_info['cuisines']
        }
        
        restaurants_data.append(extracted_info)
        
df_restaurants = pd.DataFrame(restaurants_data)

## Replace Country Code with Country Name
country_code = pd.read_excel("Data/Country-Code.xlsx")
df_restaurants = pd.merge(df_restaurants, country_code, on = "Country Code", how = "left")
df_restaurants = df_restaurants.drop(columns = "Country Code")
df_restaurants.to_csv("data/restaurants.csv", index = False)

print(f"Extraction is successful. Data is stored as 'restaurants.csv'")
print(df_restaurants.head())

restaurant_events = []

print(f"Extracting Restaurants Event Data...")

for results in data:
    for restaurants in results['restaurants']:
        restaurant_info = restaurants['restaurant']
        zomato_events = restaurant_info.get('zomato_events', []) #ignore restaurant w.o events
        event_start_date = event['start_date'].split('-') #Extract Year and Month
        event_year = int(event_start_date[0])
        event_month = int(event_start_date[1]) 
        
        for event in zomato_events:
                event = event['event']                
                if event['photos']: #Fill in N/A for those events without photos
                    photo_url = event['photos'][0]['photo']['url'] 
                else:
                    photo_url = 'N/A'
                
                if event_year > 2019 or (event_year == 2019 and event_month >= 4): #Filter March 2019 onwards
                    extracted_event_info = {
                        'Event ID': event['event_id'],
                        'Restaurant ID': restaurant_info['R']['res_id'],
                        'Restaurant Name': restaurant_info['name'],
                        'Photo URL': photo_url,
                        'Event Title': event['title'],
                        'Event Start Date': event['start_date'],
                        'Event End Date': event['end_date']
                    }
                    restaurant_events.append(extracted_event_info)
                
df_restaurant_events = pd.DataFrame(restaurant_events)
#Convert string to Date format
df_restaurant_events["Event Start Date"] = pd.to_datetime(df_restaurant_events["Event Start Date"])
df_restaurant_events["Event End Date"] = pd.to_datetime(df_restaurant_events["Event End Date"])
df_restaurant_events.to_csv("data/restaurant_events.csv", index = False)

print(f"Extraction is successful. Data is stored as 'restaurants_event.csv'")
print(df_restaurant_events.head())

rating_data = []

print(f"Extracting Restaurants Ratings Data...")

for results in data:
    for restaurants in results['restaurants']:
        rating_info = restaurants['restaurant']['user_rating']
                
        # Filter only selected Rating Text
        rating_text = rating_info['rating_text']
        if rating_text in ["Poor", "Average", "Good", "Very Good", "Excellent"]:
            extracted_info = {
                'Threshold ': float(rating_info['aggregate_rating']),
                'Rating': rating_text
            }
        
            rating_data.append(extracted_info)
        
rating_data = pd.DataFrame(rating_data)

#Calculate the threshold of each rating group
rating_threshold = rating_data.groupby(["Rating"]).min().reset_index()
rating_threshold.to_csv("data/rating_threshold.csv", index = False)

print(f"Extraction is successful. Data is stored as 'rating_threshold.csv'")
print(rating_threshold.head())

print("Data Extraction is completed.")