import requests
import json

print("Which movie do you want to see?")
movie = input()

payload = {'movie_id': movie}
r = requests.get('https://yts.lt/api/v2/movie_details.json', params=payload)

r = json.loads(r.text)
r = json.dumps(r, indent=2, sort_keys=True)

with open("test.json","w") as outfile:
    json.dump(r, outfile)

# print(r)