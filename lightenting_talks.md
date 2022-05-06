# Unit 2 Lightening Talks

## Refactoring and Clean code (Andrea)
- **Refactoring**: You should not add any new functionality
- Why? Make the code more readable, easier to maintain (avoid technical debt), improve time/space complexity
- Debugging should be done separately
- **Clean Code**: Use good variable names, use comments, functions do one thing
---
  
## MVC Pattern (Model-View-Controller) (Vera)
Example with legos // web app
- **model**: different types of legos // web app: data, code, etc
- **view**: spaceship (final product) // web app: final web page presented
- **controller**: The person building with legos; receives request // web app: request
---
## Encapsulation (Katherine)
- Hiding complexity (hide the interal state, aka information hiding)
- A class is an example of encapsulation 
- Access modifying: setting to variable/attribute to Private
- use double underscore, aka dunder `__` prior to an attribute
-  `__attribute_name`
-  How to get to the variable to change it (use getters and setters)??????
-  Why? security, data hiding, asthetics
---
## Principles of Web Design (Roshni)
- Usability
  - Nielson Norman Group 'usability 101'
  - 5 components: Learnability, Efficiency, Memorability, Errors, Satisfaction
- Readability:
  - Font size, consistency, etc; reading level (avoiding jargon, keeping simple language), heading/subheadings helpful?, text formatting
- Acessibility:
  - WCAG (Web Content Accessibility Guidelines)
  - Serving needs of ppl with disabilities
    - Certain industries must have their websites meet ADA standards 
---
## Database Transaction and Database Trigger (Natalya)
- Transaction: a logical unit that is indep executed for data reteieval
- ACID:
  - Atomic: transaction must be complete (committed-added or rolled back- undone)
  - Consistent: cannot break database's constraints
  - Isolated: 
  - Durable: 
- Trigger: A procedure in database which automatically invokes a special event
  - syntax: `create trigger <trigger_name> before/after <something> on <table_name> for <trigger_body>`
  - Example trigger:
   ```
   CREATE TRIGGER cat_adopted AFTER DELETE ON available_cats FOR EACH ROMW EXECUTE PROCEDURE after_cat_adopted();
   ```
---
## Wi-fi (Ruge)
- Radio frequencies sent (2.4 Ghz or 5 Ghz) to (?)
- Wifi Router: brodcasts a wifi signal; nearby devices can connect to this signal
- Wi-fi vs Bluetooth
  - Bluetooth: connect devices to eachother to share data
    - slower tranfser rate, shorter range, simpler to use, no password 
  - Wifi: connect devices to the internet
- Invented in 1990; IEEE 802.11

---
## Internet Browsers (Lin)
- Examples: Google Chrome, Mozilla Firefoz, Microsoft Edge, Safari
- An application used to access/view websites
- Domain youtube.com
- Domain Name System (DNS): will match domain name typed with IP address of the site
- Client (browser) must connect to the server:
  - Transmission control protocol (TCP)
- Browers also keeps info secure, 

---
## Internet Cabling and ISP (Nikki)

- Iternet is network of networks that is connected with **cables**
  - Pulses of electricity are sent to represent binary?
  - Fiber-optic cables: connect networks globally, across the ocean
  - thin (like garden hose)
  - ISP (internet service provider), ex AT&T, Verizon
    - Tier 1: internet between countries, with undersea cables
    - Tier 2:
    - Tier 3: 

---
## Modem vs. Router (Diana)
- Modem: has a unique ID (public IP address), connects your devices to your ISP.  Acts as a translator between ISP and devices (binary)
- Router: Plugs into the modem.  It creates an IP address for each device (a local IP address)
[Resource shared with diff between router and modem](https://lifewire.com/difference-between-modem-and-router-4159854)

---
## Web servers and packets (Amel)
- Web server: can be an actual computer or a ??
- Packets: data being sent over the internet in chucks
- Packet contains:
  - Header: 
  - Payload: actual data itself
  - Trailer: tells recipient that it mad it to the end

## IP Addresses (Doina)
- Internet protocol address: numerical label with a unique #
- Each IP address is unique
- IP addresses are required to browse the internet
- IPVv4 is a 32 bit number that uniques IDs a ??

## Bandwidth (Tangleap)
- **Bandwidth:** a measuremeant of how much data can be sent/recieved at a time
- **Measures capacity, not speed**
- Can be measured it bits per second
- example: streaming High def video requires > bandwith than low def video
- Throughput vs. Latency:
  - **throughput**: amount of data that can be sent/recieved in a timeframe
  - **latency**: time it takes for data to reach destination after being sent
---
## Firewall (Jodi)
- Filters data coming into your network and out of your network, onto the internet
- Example: some gvts restrict what ppl can access on internet and post to the internet.
- VPN: virtual private networks; encrypt data and make it anonymous
---
## Web Hosting (Liqing)
- Allows a website to be available to everyone -- beyond just accessed on your own computer through localhost.
- dedicated web hosting vs. VPS hosting vs. Cloud hosting
---
## Domain Name System- DNS (Amy)
- Translates domain name into IP addresses 
- domain name: name we know (ie- google, wikipedia)

## HTTP and HTTPS
- HTTP: Hypertext transfer protocol
  - HTTP cookies: a small piece of data
    - session mngmt, personalization, tracking
- HTTPS: HTTP + 'secure'
  - encryption (not sent as plain text)
  - data integrity
  - authenitication

## Sed and awk (Mitra)
- bash commands
- useful for data manipulation
- **Sed**: stream-oriented, non-interactive, text editor
- `sed 's/foo/bar/g' file`: replace foo with bar in each place in the file
- **awk**: used to manipulate columns of data

## Four Layers of Internet (Marjana)
- Application - example HTTP, sending messages between applications/web servers
- Transport
- Internet (Network layer)
- Link: (bottom layer) 

## UML: Unified Modeling Language (Ada)
- Kind of like a standardized pseudo-code
- Diagrams (several types):
  - Structural, behavioral, sequence 
- Simplifies ideas: able to see what is happening visually
- can commuinicate whats going on for ppl who aren't programmers

## Abstract Class & Interface (Olena)
- **Abstract class**: Can't be instantiated directly
- `from abc import ABC, abstractmethod` in Python
  - generalize behavior from more ??
- **Interface**: pure abstract class.  A child class must implement all the methods. (Python doesn't support?)
  - purpose: standardize behavior

## XML and JSON (Tori)
**XML**: 'eXtensible Markup Language":
  - uses **tags**, which are defined by the author
  - looks similar to HTML
  - example: `<child> </child>`
  - Has a nested structure
  - scalable: can add data in/take out, so it can change in size
  - human-readable
  - somehow more powerful  
  
**JSON**: "JavaScript Object Notation", however is language-indep
- more popular, easier to use
---
## Views and Templates in Flask (Lulu)
- Flask view: Within model-view-controller, is the view
- **Templates**: files with static data
- **Jinja**: Flask's default template engine
  - Template folder will hold templates
  - Jinja syntax (delimiters):
  - `{%.... %}` conditional `{% end for/if %}`
  - Other option: HTML folder in Template ile:
    - `import render_template`
    - call render_template: `render_template(file_name.html)`
---
## Non-Relational Databases (Ying)
- Relational databases can be overwhelmed -- have to maintain relationships (heavy on memory/processing demands)
- NoSQL (non relational databases): split workload across multiple servers.  
- Much more scalable
- Types: 
  - key-value stores (can only have two columns: key-value, ex: DynamoDB, Redis)
  - Document Stores (ex: MongoDB, CouchDB)
  - Column Family Data Stores, aka Wide Column Data Stores
  - Graph Databases 
---
## Site Maps (Joanna)
  - specific model of a website's content:
    - for users: table of content, helps to navigate (user experience)
    - for search engines: uses the site map to determine what to return for certain searches
---
## Wireframes (Fena)
- Most commonly used by UX/UI designers
- A way to show developers what the designers want the look/features to be
- clarifies website features
  - low, mid, and high fidelity: how much detail goes into it
    - low fidelity: brainstorm/sketch, not to scale
      - tools: paper/whiteboard
    - mid fidelity: more accurate to webpage/phone screen
      - tools: sketch, Figma, Adobe XD
    - high fidelity: realistic, accurate color scheme, etc
---
## SVGs (Marlyn)
- Scalable Vector Graphic
  - They do not loose quality when zoom in
  - Created with paths, have start/end 
  - Compared with Raster images:
    - load faster; made up of text
    - Can be more accessible to ppl who have visual impairments, etc (can be converted to audio)
    - A very detailed image file may be too large (so raster may be better in that case)
---
## SEO & Meta Tags (Elaine)
**SEO**: Search Enging Optimization - to improve visibility of a site on a search engine  
**SERP**: Search enging results page  
**Web Crawlers**, aka spiders: Bots operated by search engines; job is to go through and index a website.  
**Keyword Stuffing**: Adding keywords to try to get a site to appear higher in SERPs (bad practice)
- **As developers**:
  -  We can make a **sitemap**  
  -  **robots.txt**: tells crawlers things to ignore in search requests
  -  **meta tags within HTML**: Tells a serach engine what site is about. `<title> </title>`, `<meta>` 
---
## Shell Script (Nina)
**Shell scripting**: 
- Can have a file with `.sh` : file_name.sh
- Then run this file 
  - `chmod +x file_name.sh` makes this file executable (??)
- This is helpful if you want to execute many lines of code in the terminal
