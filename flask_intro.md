# Flask intro
Flask acts as a web server. It needs to be running to be able to recieve and send back responses. (<mark>Q: Is this accurate?</mark>)

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

---

## Blueprints
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
