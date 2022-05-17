# Flask intro
Flask acts as a web server. It needs to be running to be able to recieve and send back responses. 
- Flask provides patterns to define endpoints, read HTTP requests, define responses, and specifies where to put the code.

```.
├── app
│   ├── models
│   │   └── __init__.py
│   ├── __init__.py
│   └── routes.py
├── README.md
└── requirements.txt
```
**routes.py**: The responsibility of this file is to define the endpoints.  
**app/models**: This will be responsible for holding data models.

Within the app/\_\_init__\.py:
```
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)

    return app
```
**To run flask**:
`(venv) $ flask run` 
  - Looks fo rfolder called **app** and for `create_app` function.

**To run flask with debugger**:
`(venv) FLASK_ENV=development flask run`

To stop running:
`ctrl + c`

Default Flask Server URL is:
- **localhost:5000**    
- the IP address is  **127.0.0.1**
- clients will send HTTP requests to http://localhost:5000 or http://127.0.0.1
 

**side note**: if we ever need to update the requirements.txt for a project, we should run: `(venv) $ pip freeze > requirements.txt`

## Return responses:
- By default, a response with no specified status code returns 200 OK
Status code: 
---
Without blueprints, a route will be:  
@app.route("endpoint", methods=['GET', etc])
## Blueprints- can be helpful for organizing routes
within app/__init__.py
```
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    # Register Blueprints here
    from .routes import books_bp
    app.register_blueprint(books_bp)
    
    from .routes import hello_world_bp
    app.register_blueprint(hello_world_bp)

    return app
```
Instantiating Blueprint within routes.py:
```
hello_world_bp = Blueprint("hello_world_bp", __name__)  
books_bp = Blueprint("books", __name__, url_prefix="/books")
```
---
Note: flask server running elsewhere and want to find places that flask is running:   
Example error:  
`OSError: [Errno 48] Address already in use`
 
`pgrep -fla flask`  
To stop everything with flask in its argument list `pkill -fla flask`  
To kill a  particular server:  
`kill -<server_id>`  


## Handle errors in Flask
Example: 
```
@cats_bp.route("/<cat_id>", methods=["GET"])
def get_one_cat(cat_id):
    try:
        cat_id = int(cat_id)
    except ValueError:
        response = {"msg": f"Invalid id: {cat_id}.  Need a cat id number"}
        return jsonify(response), 400

    chosen_cat = None
    for cat in cats:
        if cat.id == cat_id:
            chosen_cat = cat
            break

    if chosen_cat is None:
        response = {'msg': f"Could not find a cat with id {cat_id}"}
        return jsonify(response), 404

    response = {
            'id':chosen_cat.id,
            'name': chosen_cat.name,
            'age': chosen_cat.age,
            'color': chosen_cat.color
            }

    return jsonify(response), 200
```


---
## Dev Workflow
Our dev workflow for Flask development may now look like this:
- cd into a project root folder
- Activate a virtual environment
- Check git status
- Start the server
- Cycle frequently between:
  - Writing code
  - Checking git statuses and making git commits
  - Debugging with Postman, server logs, VS Code, and more
- Stop the server
- Deactivate the virtual environment
---
**To view all current softwares/versions within your venv**: `(venv) pip freeze`

--- 
## Flask models (classes)

There should be a separate file for each model/class:  Example content in file:  
```
from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
```
---
on app/\_\_init\_\_\.py :

within **def create_app(test_config=None) function**:  
- import the models:
-  `from app.models.book import Book`   
-  `from app.models.author import Author`
---
### One-to-Many relationships:

```
class Parent(Base):
    __tablename__ = 'parent'
    id = db.Column(db.Integer, primary_key=True)
    children = relationship("Child", back_populates="parent")
```
Example parent class:
```
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    Books = db.relationship("Book", back_populates="author")
```
Example child class:
```
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    author_id = db.Column(db.Integer,db.ForeignKey('author.id'))
    author = db.relationship("Author", back_populates="books")
```

```
class Child(Base):
     __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship("Parent", back_populates="children")
```
---
## Debugging:
- `print(response.status_code)` #output: 200, 404, etc
- save api call into a variable, ie: response

