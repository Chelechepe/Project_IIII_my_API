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
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import statistics as st

app =Flask(__name__)

#we created a host link that contains mesage that is being read out of our read me 
# read me explains every rout of the API

@app.route("/")  
def index():
    readme_file = open("README.md", "r")
    md_template = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template

#we created a special feature that generates a number between 0 and 1000

@app.route("/random-number") 
def random_number():
    return str(random.choice(range(0,1000)))

# this part of the code can query the diferent characters in the series friends 
# it shows all of the characters in all seasons and episodes, 
# this can be used in /sentence/<name> to find a specific dialogue

@app.route("/characters") 
def list_all_characters():
    return jsonify(sql.list_all_characters())

# this part of the code can query the diferent episode titles in the series friends 
# it shows all of the season and episode number, 

@app.route("/episodes") 
def list_all_episodes():
    return jsonify(sql.list_all_episodes())

# Getting query on all the lines ever said from every character in friends
# by character, episode, season in ascendin order

@app.route("/line")
def all_lines ():
    return jsonify(sql.get_everything()) 

# Get everything from friends db
# we use to query to get sentences said by specific character in friends
# list of characters can be extracted from /characters

@app.route("/characters/<name>")
def character_name (name):
    return jsonify(sql.get_everything_from_someone(name)) 

# Get everything from friends db
# list all the lines filtered by season and episode title

@app.route("/season/<season>/<name>")
def get_all_by_season_name(season, name):
    return jsonify(sql.get_all_by_season_name(season, name)) 

# Get everything from friends db
# list all the lines filtered by season and episode title

@app.route("/episodes/<season>/<episode_title>")
def get_all_by_season_episode(season,episode_title):
    return jsonify(sql.get_all_by_season_episode(season,episode_title)) 

# Get everything FROM someone: SQL & argument
# list all the lines filtered by season and episode title by character
# it contains the parameters for language translator

@app.route("/episodes/<season>/<episode_title>/<name>")
def get_all_by_season_episode_name (season,episode_title,name):
    test = jsonify(sql.get_all_by_season_episode_name(season,episode_title,name)) 
    all = test.get_json()
    if 'language' in request.args.keys():
        for one in all:
            language = request.args["language"]
            trans = googletrans.Translator()
            result = trans.translate(one["quote"], dest=language)

            one["quote"] = result.text
    return all

#lets do sentiments bitches!
# we use the number of the season and the number of the episode to identify
# the sentiment that the episode has.

@app.route("/sentiment/<season>/<episode_number>")
def get_sentiment_season(season,episode_number):
    sese = jsonify(sql.get_sentiment_season(season,episode_number)) 
    all = sese.get_json()
    sentimentdf = pd.DataFrame.from_dict(all)
    nltk.downloader.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
    
    def sa(x):
        try:
            return sia.polarity_scores(x)
        except:
            return x

    sentimentdf["sent_score"] = sentimentdf["quote"].apply(sa)
    sentiment=[]

    for sent in sentimentdf["sent_score"]:
            sentiment.append(sent["compound"])

    feelings = round(st.mean(sentiment),4)

    if feelings == 0:
        return f"We have a sentiment indicator of {feelings}, meaning this episode was NEUTRAL"
    elif feelings > 0:
        return f"We have a sentiment indicator of {feelings}, meaning this episode was SOMEWHAT POSITIVE"
    elif feelings > 0.25:
        return f"We have a sentiment indicator of {feelings}, meaning this episode was POSITIVE"
    elif feelings > 0.50:
        return f"We have a sentiment indicator of {feelings}, meaning this episode was VERY POSITIVE"
    elif feelings < 0:
        return f"We have a sentiment indicator of {feelings}, meaning this episode was SOMEWHAT NEGATIVE"
    elif feelings < -0.25:
        return f"We have a sentiment indicator of {feelings}, meaning this episode was NEGATIVE"
    elif feelings < -0.50:
        return f"We have a sentiment indicator of {feelings}, meaning this episode was VERY NEGATIVE"
    else:
        return "No sentiment detected"

# we use the number of the season and the number of the episode to identify
# the sentiment that a character has in a specific the episode has.

@app.route("/charactersentiment/<season>/<episode_number>/<name>")
def get_sentiment_episode(season,episode_number,name):
    sese = jsonify(sql.get_sentiment_episode(season,episode_number,name)) 
    all = sese.get_json()
    sentimentdf = pd.DataFrame.from_dict(all)
    nltk.downloader.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
    
    def sa(x):
        try:
            return sia.polarity_scores(x)
        except:
            return x

    sentimentdf["sent_score"] = sentimentdf["quote"].apply(sa)
    sentiment=[]

    for sent in sentimentdf["sent_score"]:
            sentiment.append(sent["compound"])

    feelings = round(st.mean(sentiment),4)

    if feelings == 0:
        return f"{name} has a sentiment indicator of {feelings}, meaning this episode was NEUTRAL in Season {season} Episode {episode_number}."
    elif feelings > 0:
        return f"{name} has a sentiment indicator of {feelings}, meaning this episode was SOMEWHAT POSITIVE in Season {season} Episode {episode_number}."
    elif feelings > 0.25:
        return f"{name} has a sentiment indicator of {feelings}, meaning this episode was POSITIVE in Season {season} Episode {episode_number}."
    elif feelings > 0.50:
        return f"{name} has a sentiment indicator of {feelings}, meaning this episode was VERY POSITIVE in Season {season} Episode {episode_number}."
    elif feelings < 0:
        return f"{name} has a sentiment indicator of {feelings}, meaning this episode was SOMEWHAT NEGATIVE in Season {season} Episode {episode_number}."
    elif feelings < -0.25:
        return f"{name} has a sentiment indicator of {feelings}, meaning this episode was NEGATIVE in Season {season} Episode {episode_number}."
    elif feelings < -0.50:
        return f"{name} has a sentiment indicator of {feelings}, meaning this episode was VERY NEGATIVE in Season {season} Episode {episode_number}."
    else:
        return "No sentiment detected"

# we use the number of the season and character to identify
# the sentiment that character during the season.

@app.route("/seasons/charactersentiment/<season>/<name>")
def get_sentiment_season_character(season,name):
    sese = jsonify(sql.get_sentiment_season_character(season,name)) 
    all = sese.get_json()
    sentimentdf = pd.DataFrame.from_dict(all)
    nltk.downloader.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
    
    def sa(x):
        try:
            return sia.polarity_scores(x)
        except:
            return x

    sentimentdf["sent_score"] = sentimentdf["quote"].apply(sa)
    sentiment=[]

    for sent in sentimentdf["sent_score"]:
            sentiment.append(sent["compound"])

    feelings = round(st.mean(sentiment),4)

    if feelings == 0:
        return f"{name} has a sentiment indicator of {feelings}, meaning it was NEUTRAL in Season {season}."
    elif feelings > 0:
        return f"{name} has a sentiment indicator of {feelings}, meaning it was SOMEWHAT POSITIVE in Season {season}."
    elif feelings > 0.25:
        return f"{name} has a sentiment indicator of {feelings}, meaning it was POSITIVE in Season {season}."
    elif feelings > 0.50:
        return f"{name} has a sentiment indicator of {feelings}, meaning it was VERY POSITIVE in Season {season}."
    elif feelings < 0:
        return f"{name} has a sentiment indicator of {feelings}, meaning it was SOMEWHAT NEGATIVE in Season {season}."
    elif feelings < -0.25:
        return f"{name} has a sentiment indicator of {feelings}, meaning it was NEGATIVE in Season {season}."
    elif feelings < -0.50:
        return f"{name} has a sentiment indicator of {feelings}, meaning it was VERY NEGATIVE in Season {season}."
    else:
        return "No sentiment detected"

#this will check that the name is the meain
# we can define the port, port = 3000 and asignes the address
# debug= True/False, when you change something it updates

if __name__ == '__main__': 
    app.run(debug=True) 