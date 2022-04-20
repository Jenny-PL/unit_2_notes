## Python request package:
[Documentation about using request package in python](https://docs.python-requests.org/en/master/)    

[quick start for request package](https://docs.python-requests.org/en/master/user/quickstart/)
- `import requests` at top of file
- `path = url`
- `key = access_token`
- `query_params = {key:value, key:value}`
- `response = request.get(path, params=query_params)`
- `response.json()` : turns code from json to python data structure
- **Tip**: use a breakpoint, placed at time of calling response, and step into funciton with debugger, to inspect the api's response.
  
---
# RESTful APIs
**REST** = representaional state transfer
- Design principal preferring reliable/predicable endpoints that focus on resources.  
- Uses HTTP (vs. SOAP or something else)
- Mainains **statelessness** of the server... will not track data about the user between requests
- returns a standard media type (JSON, HTML, etc)
- has a **uniform interface** and resource based paths (endpoints are based on resources)
  

**CRUD**: Create, Read, Update, Delete

- 