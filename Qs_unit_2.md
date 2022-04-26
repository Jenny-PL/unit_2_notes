# creating endpoints:
This works:
```
@books_bp.route("/<book_id>", methods=["GET"])
```
However, this did not:
```
@books_bp.route("/:book_id", methods=["GET"])
```
Q: why? (We saw the :id syntax in unsplash api)  

Q: Does Flask ignore the < > around the variable?.  

Q: Why is this in quotes, when it is a variable?  Does it always read in as a string?
---

Q: running into trouble at error handling (api_books_2a). Getting attribute error re: tuples. why?

---
Q: from api_reqeust.py, why is json() not being used?
 -- Also, I used `FLASK_ENV=development flask run` to run flask, then pressed 'play' button to run this code, but only got:   
 `/usr/local/bin/python3 /Users/jennyluong/Developer/projects/classroom/unit_2_notes/api_request.py`    
 - How to do I run the code within flask on, to see status code in terminal?