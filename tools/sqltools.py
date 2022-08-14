from config.sqlconfig import engine
import pandas as pd

## GET all the information of the data base
def get_everything ():
    query = (f"""SELECT *FROM friends;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

## GET one characters list of coments the data base
def get_everything_from_someone(name):
    query = (f"""SELECT * FROM friends WHERE author = "{name}";""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

## GET list of all characters in the data base
def list_all_characters():
    query = (f"""SELECT author FROM friends.friends group by author;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

## GET list of all episode in the data base
def list_all_episodes():
    query = (f"""SELECT season, episode_number, episode_title FROM friends.friends group by episode_title order by season asc;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

## GET all quotes in a given episode by season in the data base
def get_all_by_season_episode(season,episode_title):
    query = (f"""SELECT * FROM friends.friends WHERE season = {season} and episode_title = "{episode_title}" order by quote_order asc;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

## GET all quotes in a given season by character in the data base
def get_all_by_season_name(season,name):
    query = (f"""SELECT * FROM friends.friends WHERE season = {season} and author = "{name}" order by quote_order asc;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

## GET all quotes in a given episode by season by character in the data base
def get_all_by_season_episode_name(season,episode_title,name):
    query = (f"""SELECT * FROM friends.friends WHERE season = {season} and episode_title = "{episode_title}" and author = "{name}" order by quote_order asc;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

## GET all quotes in a given episode by season by character in the data base
    #we will use this to filter the sentiment of a character per season per espisode
def get_sentiment_episode(season,episode_number,name):
    query = (f"""SELECT * FROM friends.friends WHERE season = {season} and episode_number = "{episode_number}" and author = "{name}" order by quote_order asc;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

    #we will use this to filter the sentiment of a episode per season
def get_sentiment_season(season,episode_number):
    query = (f"""SELECT * FROM friends.friends WHERE season = {season} and episode_number = "{episode_number}" order by quote_order asc;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')


## POST
def new_message (author, episode_number, episode_title, quote, quote_order, season):
    engine.execute(f"""
    INSERT INTO friends (author, episode_number, episode_title, quote, quote_order, season)
    VALUES ('{author}', '{episode_number}', '{episode_title}', '{quote}', '{quote_order}', '{season}');
    """)
    return f"Correctly introduced: {author} {episode_number} {episode_title} {quote} {quote_order} {season}"