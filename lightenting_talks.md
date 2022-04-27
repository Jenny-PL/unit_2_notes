# Unite 2 Lightening Talks

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
