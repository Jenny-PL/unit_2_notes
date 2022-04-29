## API 3 homework, within Create and Read All Books:
1. Within hello-books-api/app/routes:  
 Both of these seemed to show up... which is right? Do both work? Why?    

    `books_bp = Blueprint("books_bp", __name__, url_prefix="/books")`     

    `books_bp = Blueprint("books", __name__, url_prefix="/books")`

2. Postman worked with a GET request, however localhost on website gave error: 'can't provide a secure server'. What does this mean?

# Review Topics with lingering Q's:
- **pytest.raises()**: How to use this??
- **Try/except, raising errors**, etc... general confusion as far as how to best implement, when to use one vs. other
  - Cannot return errors... why?
    - [sea turtle- exception handling](https://adaacademy.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=ac6089c2-01f8-43e7-9c6f-ae610133e220)
- **Classes**... need more practice
  - inheritance & composition
    - [seat_turtle class](https://adaacademy.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d16d854e-fbd5-4849-ab86-ae6e01375c61)
  - Decorators, etc:
    - [sea_turtle class](https://adaacademy.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=2348a1bb-3840-4ba0-a03a-ae700135ebc0)
- **Big O: time/space complexity**
  - [sea turtles](https://adaacademy.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=e56d5401-7d2b-485c-9c25-ae670141fe04)
- Lists & memory
  - [sea turtle part 1](https://adaacademy.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=42cfd179-e9a6-4ae3-9afc-ae68013492f9)
  - [sea turtle part 2](https://adaacademy.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=f43d6b27-7b4d-4750-a0c9-ae6801337fdd)