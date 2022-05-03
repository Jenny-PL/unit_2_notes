## PUT method (updating part of a record):

Our endpoint will need to:
1. Read the book_id in the request path
2. Retrieve the Book instance with the matching book_id from the database
3. Read the new, updated book data from the HTTP request
4. Update the instance of Book with the new data
5. Save the updated Book in the database
6. Send back a response
   
```
@books_bp.route("/<book_id>", methods=["PUT"])
def update_book(book_id):
    book = validate_book(book_id)

    request_body = request.get_json() # this changes JSON --> python dict

    book.title = request_body["title"] # uses OOP to make updates to dict
    book.description = request_body["description"]

    db.session.commit() 
    # must do this anytime a SQLAlchemy model has been updated

    return make_response(f"Book #{book.id} successfully updated")
```
---
## DELETE method:

```
@books_bp.route("/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = validate_book(book_id)

    db.session.delete(book)
    db.session.commit()

    return make_response(f"Book #{book.id} successfully deleted")
```
---
## Query Params:
[More info on querying- from the documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/#querying-records)  

example: ht<span>tps:/</span>/my-beautiful.site/search **?category=novels** 
- Query param key:value are category: novels

Example with multiple params:
htt<span>ps:/</span>/my-beautiful.site/search **?category=novels&minimum_pages=800&maximum_pages=8000** 
  - An **&** connects the key:value pairs.

**URL Encoding** is necessary for certain characters that occuring in a URL (example: &, ?, or spaces):
ht<span>tps:/</span>/my-beautiful.site/search?name=Hand-crafted%20exclusive%3A%20finest%20tote%20bag%21
- In this case:
  - **%20** replaces (space) 
  - **%3A** replaces :
  - **%21** replaces !

To get query params from a request using Flask:
```
query_param_value = request.args.get(query_param_key)
```

The code below adds in the ability query by title:
localhost:5000/books?title=<actual_title>  

Example: ht<span>tp:/</span>/localhost:5000/books?title=The%20Land%20Before%20Time  
**returns:**  
[{"description":"A cute dino book","id":5,"title":"The Land Before Time"}]

```
@books_bp.route("", methods=["GET"])
def read_all_books():

    # this code replaces the previous query all code
    title_query = request.args.get("title")
    if title_query:
        books = Book.query.filter_by(title=title_query)
    else:
        books = Book.query.all()
    # end of the new code

    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })

    return jsonify(books_response)
```
**Note: limiting query results:**
```
Book.query.limit(100).all()
```
where limit() holds the limit #



