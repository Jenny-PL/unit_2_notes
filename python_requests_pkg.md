## Python requests package:
[Documentation about using request package in python](https://docs.python-requests.org/en/master/)    

[quick start for request package](https://docs.python-requests.org/en/master/user/quickstart/)
- **Concept**: when using requests package, python is the **client** to the API/webserver.
  
- You must **pip install** request into your virtual environment:  
```
 $ python -m pip install requests
 ```  
- `import requests` at top of file
- `path = url`
- `key = access_token`
- `query_params = {key:value, key:value}`
- `response = request.get(path, params=query_params)`
- `response.json()` : turns code from json to python data structure

- **Tip**: use a breakpoint, placed at time of calling response, and step into funciton with debugger, to inspect the api's response.
  
---

Note: 'JSON viewer awesome' [Dev tool- free, chrome extension to view JSON in tree structure](https://chrome.google.com/webstore/detail/json-viewer-pro/eifflpmocdbdmepbjaopkkhbfmdgijcc?hl=en-US)

Example from 100days of Python using [International Space Station API](http://open-notify.org/Open-Notify-API/ISS-Location-Now/)
```
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
```
