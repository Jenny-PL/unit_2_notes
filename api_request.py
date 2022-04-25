# ISS location API: http://open-notify.org/Open-Notify-API/ISS-Location-Now/
import requests
import json

# response = request.get(path, params=query_params)
response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()
print(response.status_code)  

print(f"The timestamp is: {data['timestamp']}")
print(data['iss_position'])
print('************')
print(data['iss_position']['latitude'], data['iss_position']['longitude'])

longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']
coordinates = (f"({round(float(longitude),2)}, {round(float(latitude),2)})")
print(coordinates)

response.raise_for_status() 
# this will raise error if an error occurs, with HTTP status-- 
# Note: does not seem to work

# Example prints:
#   The timestamp is: 1650897304
# -36.2524 20.1328

'''
Example from the website:
import urllib2
import json

req = urllib2.Request("http://api.open-notify.org/iss-now.json")
response = urllib2.urlopen(req)

obj = json.loads(response.read())

print obj['timestamp']
print obj['iss_position']['latitude'], obj['data']['iss_position']['latitude']

# Example prints:
#   1364795862
#   -47.36999493 151.738540034
# '''