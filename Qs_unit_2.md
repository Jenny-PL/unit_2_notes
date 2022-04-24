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
