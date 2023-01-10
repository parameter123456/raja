import json

import requests

api_key = 'c: http://www.omdbapi.com/?i=tt3896198&apikey=2d8f4cc8'
title = "king"
url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"
response = requests.get(url)
data = json.loads(response.text)

# Print out the movie's information
print(f"Title: {data['title']}")
print(f"Year: {data['Year']}")
print(f"Rated: {data['Rated']}")
print(f"Plot: {data['Plot']}")
