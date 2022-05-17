# Models, using SQLAlchemy, Alembic, etc...
- SQLAlchemy wil connect postgres app and flask
- Object Relational Mapper (ORM)
- Instance in a class corresponds to a record in a table
- **Model** represents one concept relevten tot the app (defines state and behavior)
  - A class that talks to a database
- Database migration (aka schema migration): changes to the schema/data table

## Run postgres:

```
psql -U postgres
```
## Create a database
```
CREATE DATABASE hello_books_development;
```
```
 \q
 ```
 ## Connecting DB to flask
 ```
 # connection string:
 postgresql+psycopg2://postgres:postgres@localhost:5432/REPLACE_THIS_LAST_PART_WITH_DB_NAME
```
In this case:

```
postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development
 ```
To top of folder app/__init__.py
```
from flask_sqlalchemy  
import SQLAlchemy  
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
```
withinin create_app(test_config=None) function:
```
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# here is the connection string:
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

db.init_app(app)
migrate.init_app(app, db)
```

## Making model (class):
```
# there should be a separate folder for each class/model
from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key= True, autoincrement= True)
    title = db.Column(db.String)
    descrption= db.Column(db.String)
    __tablename__ = "books" 
    # __tablename__ wasn't here, class would automatically be named 'book'

    def to_string(self):
        return f"{self.id}: {self.title}. Desription: {self.descrption}"
```
## Initiate
One time Init Set up
```
(venv) $ flask db init
```
Generate Migrations After Each Model Change
```
(venv) $ flask db migrate -m "adds Book model"
```
When running this command ourselves, we should replace the "adds Book model" with a description relevant to our recent changes.... this is similar to text with a git commit.

Next, run this separate command to actually run and apply the generated migrations:

```
(venv) flask db upgrade
```
A **migrations** folder will appear within your project's root folder.    

Now you can go to postgres to see your data base:
```
(venv) psql -U postgres
```
## General step by step:
1. create database in postgres
2. connect database and Flask
3. create model files
   1. create a class for each model
   2. define state/behavior of the model
4. Initialize migrations: create instrutions to modify database
   1. Only do this one time
5. Generate migrations & apply migrations: apply instructions
   1. Do this after making a new model, or changes to table/schema