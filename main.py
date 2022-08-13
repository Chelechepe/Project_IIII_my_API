from flask import Flask
import random
from pymongo import MongoClient
import pymongo
import tools.sqltools as sql
from flask import jsonify
from os import name
from flask import Flask, request, jsonify
import markdown.extensions.fenced_code
import pandas as pd
import json
import random
import googletrans

app =Flask(__name__)

@app.route("/")  #we created a host link that contains msg
def index():
    readme_file = open("README.md", "r")
    md_template = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template

@app.route("/random-number") #we created a special feature that generates a number between 0 and 1000
def random_number():
    return str(random.choice(range(0,1000)))

if __name__ == '__main__': #this will check that the name is the meain
    app.run(debug=True) # we can define the port, port = 3000 and asignes the address
                # debug= True/False, when you change something it updates
