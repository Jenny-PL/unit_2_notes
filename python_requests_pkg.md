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