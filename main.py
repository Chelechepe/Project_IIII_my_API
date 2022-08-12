from flask import Flask
import random
from pymongo import MongoClient
import pymongo
import tools.mongotools as mongo
from flask import jsonify

app =Flask(__name__)

@app.route("/")   #we created a host link that contains msg
def greetings ():
    return f"How are you doing?"

@app.route("/random-number") #we created a route that displays a number
def random_number():
    return str(random.choice(range(0,11)))

@app.route("/campus/<location>") #this would be another rout for location
def campus_location(location):
    if location == "BCN":
        return "Carrer Pamplona 96"
    elif location == "MAD":
        return "Paseo de la Chopera, 14"

@app.route("/line/<name>")
def all_from_mongo(name):
    lines = mongo.all_sentences(name)
    return jsonify(lines)


if __name__ == '__main__': #this will check that the name is the meain
    app.run(debug=True) # we can define the port, port = 3000 and asignes the address
                # debug= True/False, when you change something it updates


test 23