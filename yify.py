import requests
import json

print("Which movie do you want to see?")

movie = input()
payload = {'movie_id': movie}

r = requests.get('https://yts.lt/api/v2/movie_details.json', params=payload)
response = json.loads(r.text)

print(response)