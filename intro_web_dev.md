# Web Dev
Note: <mark> cmd+alt+i </mark>to inspect page for html/css/network requests, etc
- **Front end**: user interaction, what you see/click on
- **back end**: data, logic
- **end user, aka client**: brower/computer
- **backend API**: translates between a web server adn as user (which may be another program)
- **data base**: holds data/info
- **API**: Application programming interface. Is an interface that replays messages from software A to software B.  (Software could be application, database, browser, devices, etc.. )
  - If there's a button or URL path, there's an API behind it. 
    - ie- to read the NYT top stories, we use the NYT Top Stories API:
    - [NYT Top stories API](https://developer.nytimes.com/docs/top-stories-product/1/overview)
    - [NYT APIs](https://developer.nytimes.com/apis)
---
## Client-server model
- **Client**: ac computer who sends request for a resource to a server  
- **Server**: Another computer who:
   1. receives the request 
   2. sends back a response
- **Webserver**: Place where a website's data and logic is kept; may be on several computers or just one computer (this is separate form the client. <mark> ?always separate... could one computer have both the client and webserver?</mark>)
- **HTTP (Hypertext Transfer Protocol)**: specific set of rules the webistes follow in order to send and recieve data
- **sequence diagram**: shows request-response cycle
  - lucidchart
  - draw.io
- **client** (request)--> <--(response) **server** (request) --> <-- (response) **database**
- **endpoint**: 'path' or url to a resources
---

## HTTP request: 
- Must contain: method, path
- May contain: headers, querry, body
- **Method**: GET, POST, PATCH, DELETE
- **Path**: aka url request
- **Querry parameters**: key-value pairs that make a request more specific 
- **Headers**: colon separated pairs of info
- **Body**: additional resources to be sent to the server
---
## HTTP response
- Must contain status code, status msg
- May contain HTTP headers, body
- **status code**
  - [complete list of status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
  - 100-199: info response; not commonly seen
  - 200-299: successful response
    - 200 OK
    - 201 Created
  - 300-399: Redirects; requested resouce has been moved
    - 301: Moved permamently
  - 400-499: Client errors; request has an error
    - 404: Not found
  - 500-599: Server errors; server recieved the reqeust however cnanot create a successful response
    - 500: Internal server error
  - [funny cat pics with codes](http.cat)  
  - [funny dog pics with codes](httpstatus.dogs.com)
- **status message** 
  - Examples: OK, Created, Moved Permamently, Not found, Internal Server Error
- **HTTP headers**
- **HTTP body**
---
### Side note: URI vs URL vs URN
-**URI** is a uniform resouce identifier.  Within this broader category fall URL and URN (ie- google.com)
   - **URL** is more specific uniform resource locator (https://gooogle.com)
   - **URN** uniform resouce name 


