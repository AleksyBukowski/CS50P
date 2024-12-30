import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit(f"1 additional argument expected, {len(sys.argv)-1} provided")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

# print(json.dumps(response.json(), indent=2))
# print(o["results"][0]["trackName"])

o = response.json()

for result in o["results"]:
    print(f'{result["artistName"]} - {result["trackName"]}')


