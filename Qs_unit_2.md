# API 3 homework, within Create and Read All Books:
Within hello-books-api/app/routes:

Both of these seemed to show up... which is right? Do both work? Why?  
`books_bp = Blueprint("books_bp", __name__, url_prefix="/books")`   
`books_bp = Blueprint("books", __name__, url_prefix="/books")`

### Postman worked with a GET request, however localhost on website gave error: 'can't provide a secure server'. What does this mean?