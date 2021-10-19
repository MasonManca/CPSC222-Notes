import requests
import json

api_key = "MdVL6OVMW0VuUZqAH6HmKqJxcGyHx74D"

url = "http://www.mapquestapi.com/directions/v2/route"

# we need a key, from, to
url += "?key=" + api_key
url += "&from=spokane"
url += "&to=seattle"

print(url)
response = requests.get(url=url)
print(response.text)
# task: extract the distance and duration from the response

json_obj = json.loads(response.text)

route_obj = json_obj["route"]
distance = route_obj["distance"]
print(distance)