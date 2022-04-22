# Load balancers
- may also be called Application Delivery Controlers (ADCs)  

**Role**: Distribute requests from clients to a **what** over the available servers, to avoid over-burdening servers and maximize speed and function.  As new servers are added, route traffic to those servers.  If a server has a malfunction, re-route that traffic.

**How does it work?**  There are several different algorithms for determining how to distrubute requests among servers.

**Who will be dealing with load balancers?**
- DevOps typically
- Maybe you, if there is a load balancer prob when you're 'on call'

**Who provides the software?**
- AWS: load balancers can be included in this service
- Nginx
- Kemp
- Citrix
- 

**Software vs hardware** loadbalancers

Some resources:
[medium article with embedded videos](https://medium.com/nerd-for-tech/explained-load-balancer-89edc6d1f444)

[youtube basic video- start here](https://www.youtube.com/watch?v=gMIslJN44P0)

[videos/info from Citrix](https://www.citrix.com/solutions/app-delivery-and-security/load-balancing/what-is-load-balancing.html)

[lots of info, from AvineNetworks](https://avinetworks.com/what-is-load-balancing/#:~:text=Load%20Balancing%20Definition%3A%20Load%20balancing,applications%20and%20websites%20for%20users)