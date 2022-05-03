# 1. set up a virtual environment
# 2. Install Flask: `pip install Flask`
# 3. in terminal: `export FLASK_APP=main.py`
# 4. then: `flask run`

# Questions: 
# /search endpoint: how to search for cafes in a location using params?
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration, aka making the Cafe Model/class
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")
    
## HTTP GET - Read Record
@app.route("/random",methods=["GET"])
def get_random_cafe():
    cafes = Cafe.query.all() # this will get all instances of cafe, I think
    # cafes = db.session.query(Cafe).all()  # answer provided by course
    cafe = random.choice(cafes) # gets a random cafe
    return jsonify({
            'id': cafe.id,
            'name' :cafe.name,
            'map_url': cafe.map_url,
            'img_url': cafe.img_url,
            'location': cafe.location,
            'seats' : cafe.seats,
            'has_toilet' : cafe.has_toilet,
            'has_wifi' : cafe.has_wifi,
            'has_sockets' : cafe.has_sockets,
            'can_take_calls': cafe.can_take_calls,
            'coffee_price': cafe.coffee_price

    }), 200

@app.route("/cafes", methods=["GET"])
def get_all_cafes():
    cafes = Cafe.query.all()

    # one-line option, using .to_dict() method and list comprehension:
    # however, gave me an error?
    # return jsonify(cafes=[cafe.to_dict() for cafe in cafes]), 200

    cafe_list = []
    for cafe in cafes:
        cafe_list.append({
            'id': cafe.id,
            'name' :cafe.name,
            'map_url': cafe.map_url,
            'img_url': cafe.img_url,
            'location': cafe.location,
            'seats' : cafe.seats,
            'has_toilet' : cafe.has_toilet,
            'has_wifi' : cafe.has_wifi,
            'has_sockets' : cafe.has_sockets,
            'can_take_calls': cafe.can_take_calls,
            'coffee_price': cafe.coffee_price
    })
    return jsonify(cafe_list), 200

# response = request.get(path, params=query_params)
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# data = response.json()

# example on how to query for one book:
# book = Book.query.filter_by(title="Harry Potter").first()

# Trying to search for one cafe by location
# http://localhost:5000/search?location=Peckham  # how to do this?
@app.route("/search", methods=['GET'])
def search_by_location():
    response = request.get("http://localhost:5000/search", params=query_params)
    query_params = {
        'location': cafe.location
    }
    cafes = Cafe.query.all() # redundent with response above.
    cafes_at_location = []
    for cafe in cafes:
        if cafe.location == query_params['location']: # how to do this?
            cafes_at_location.append({
            'id': cafe.id,
            'name' :cafe.name,
            'map_url': cafe.map_url,
            'img_url': cafe.img_url,
            'location': cafe.location,
            'seats' : cafe.seats,
            'has_toilet' : cafe.has_toilet,
            'has_wifi' : cafe.has_wifi,
            'has_sockets' : cafe.has_sockets,
            'can_take_calls': cafe.can_take_calls,
            'coffee_price': cafe.coffee_price
    })
    return jsonify(cafes_at_location), 200
    
## HTTP POST - Create Record
@app.route("/", methods=['POST'])
def add_a_cafe():
    request_body = request.get_json()
    new_cafe = Cafe(id=request_body['id'],name=request_body['name'], map_url=request_body['map_url'],
    img_url=request_body['img_url'], location=request_body['location'], seats=request_body['seats'],
    has_toilet=request_body['has_toilet'], has_wife=request_body['has_wifi'], 
    has_sockets=request_body['has_sockets'], can_take_calls=request_body['can_take_calls'],
    coffee_price=request_body['coffee_price'])
    # How can this be done without typing in all of the above??  
    db.session.add(new_cafe)
    db.session.commit()
    return {
        'response': f'Sucessfully added a new cafe: {new_cafe.name}. The cafe id is: {new_cafe.id}'
    }, 201


## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
