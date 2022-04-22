[Article with helpful API design tips](https://www.coderslexicon.com/8-tips-to-a-better-api-design/)

[RESTful API best practice article](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)

[Restful API Tutorial/vidoes](https://restapitutorial.com/)

**API process**: client (web browser) makes an HTTP request -- > to an API server (another machine).  The API server returns a HTTP response to the client.
# RESTful APIs

**REST** = representaional state transfer
- Design principal preferring reliable/predicable endpoints that focus on resources.  
- Uses HTTP (vs. SOAP or something else)
- Mainains **statelessness** of the server... will not track data about the user between requests
- returns a standard media type (JSON, HTML, etc)
- has a **uniform interface** and resource based paths (endpoints are based on resources)
  

**CRUD**: Create, Read, Update, Delete

---
Example requests/responses for an imaged app (focusing on connecting runners with each other):

1. **Requesting a runner that exists**  
HTTP Request: GET /runners/55, no request body  
HTTP Response: 200 OK  
Response body (JSON):  
{
    "name": "Emuna Smith",
    "id_num": 55,
    "pace-group": "group_3"
    "neighborhood": "White Center, Seattle, WA"
}
2. **Requesting an runner that does not exist**  
HTTP Request: GET /runners/200, no request body  
HTTP Response: 404 Not found, no response body

3. **Requesting a list of resources**  
HTTP request: GET /runners  
HTTP Response: 200 OK  
Response body:   
list of dictionaries containing all runners, see above example 1 for info included within dict [ {runner_1 details}, {runner_2 details}]

4. **Deleting a resource that exists**:  
HTTP request: DELETE /runners/55, no HTTP body  
HTTP response: 200 OK, no HHTP body

5. **Deleting a resource that does not exist**  
HTTP request: DELETE /runners/200, no request body  
HTTP response: 404 Not found, no response body

6. **Creating a new resource**  
HTTP request: POST /runners  
request body (JSON):  
{
    "name": "Edith Tims",
    "id_num": 55,
    "pace-group": "group_3"
    "neighborhood": "White Center, Seattle, WA"
}  

    HTTP response: 201 Created, no response body

---
## Class examples of API designs:
### Bookstore
![HTTP response/request table for bookstore](http.request.response.png)
### Planets
![Planets HTTP response/request table](http.request.response.Planets.png)
---
## API Keys
- To get a key, one generally has to create an account and apply for a key, then find the key within the website while logged in.  
- The key can be added as a request header, a query parameter, or inside a cookie (At Ada, we'll generally add them to the HTTP request as a query param).   
- APIs may have **rate limits**, which limit the # of calls (requests) that a client can make within a given time frame.