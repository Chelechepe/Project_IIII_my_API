________________________________________________
</br>

# Project IV My API
## API - SQL query for Friends the show
________________________________________________
</br>

#### By: Edgard Cuadra
#### Date: August 13st 2022
</br>
________________________________________________

### My Firends TV Show - API query 

<p align="Left" width="100%">
    <img width="63%" src="https://raw.githubusercontent.com/Chelechepe/Project_IV_my_API/main/images/friends_logo.gif">
</p>
</br>

### Main Endpoint page for the API query: 
        http://127.0.0.1:5000/  

### 1 - Endpoint route for generating a Random Number:
As a special feature we created a special feature that generates a number between 0 and 1000</br>
this special feature is just to test the access to the endpoint route</br>

        http://127.0.0.1:5000/random-number 

### 2 - Endpoint route for dictionary of all lines from the Show:
Getting query on all the lines ever said from every character in friends</br>
by character, episode, season in ascendin order from the first episode</br>
to the last episode of the show.</br>

        http://127.0.0.1:5000/line

### 3 - Endpoint route for dictionary of all the characters that apear in Show:
Get the query of all the diferent characters in the series friends </br>
it shows all of the characters in all seasons and episodes</br>
characters can be a features star, supporting cast of multiple charactres at once</br> 
this can be used in /sentence/< name > to find a specific dialogue </br>

        http://127.0.0.1:5000/characters 


### 4 - Endpoint route for Character sentimient in a given episode:
Get the query of all the diferent characters in a series episode</br>
we use the number of the season and the number of the episode to identify</br>
the sentiment that a character has in a specific the episode has. </br>

        http://127.0.0.1:5000/charactersentiment/<season>/<episode_number>/<name>

         example: 

            http://127.0.0.1:5000/charactersentiment/2/2/Ross

        note: this would access the sentiment of all Ross's lines 
        in season 2 episode 2 

            
### 5 - Endpoint route for Character Name:
Gets the query of all the diferent characters in the show and lines said by them. </br>
list of characters can be extracted from /characters</br>
see "3 - Endpoint route for dictionary of all the characters that apear in Show"</br>

        http://127.0.0.1:5000/characters/<name>

        example: 

            http://127.0.0.1:5000/characters/Ross

        note: this would query all Ross's lines in the Friends TV show 

### 6 - Endpoint route for all the names of the episode:
Gets the query of all the diferent part of the code can query the diferent episode titles in the series friends</br>
it shows all of the season and episode number</br>

        http://127.0.0.1:5000/episodes 

### 7 - Endpoint route for all the lines in a specific episode:
Get everything from friends db</br>
list all the lines filtered by season and episode title</br>
this rout can be used in conjunction with the</br>
route http://127.0.0.1:5000/episodes</br>

        http://127.0.0.1:5000/episodes/<season>/<episode_title>

        example: 

            http://127.0.0.1:5000/episodes/2/Ross's%20New%20Girlfriend

        note: this would query all lines in the Friends TV 
        show season 2 in episode "Ross's New Girlfriend"

### 8 - Endpoint route for lines of a Character from a given episode and season:
Get list of all the lines filtered by season and episode title by character</br>
it contains the parameters for language translator</br>

        http://127.0.0.1:5000/episodes/<season>/<episode_title>/<name>

        example: 

            http://127.0.0.1:5000/episodes/2/Ross's%20New%20Girlfriend/rachel

        note: this would query all the Rachel's lines in the Friends TV 
        show season 2 in episode "Ross's New Girlfriend"
    
    Language Translator parameter:

        http://127.0.0.1:5000/episodes/<season>/<episode_title>/<name>?language=es

        example: 

            http://127.0.0.1:5000/episodes/2/Ross's%20New%20Girlfriend/rachel?language=es

        note: this would query all the Rachel's lines in the Friends TV 
        show season 2 in episode "Ross's New Girlfriend" in the lenguage spanish

        List of all Googletranslate languages abreviatios:
        https://sites.google.com/site/opti365/translate_codes

### 9 - Endpoint route for all lines said by character in season:
Get list all the lines said by a character in a whole season of Friends Tv Show</br>

        http://127.0.0.1:5000/season/<season>/<name>

        example: 

            http://127.0.0.1:5000/season/2/Ross
        
        note: this would query all the Ross's lines in the Friends TV for
        show season 2 

### 10 - Endpoint route for sentiment of a given character in a season:
Use the number of the season and character to identify</br>
the sentiment that character during the season.</br>

        http://127.0.0.1:5000/seasons/charactersentiment/<season>/<name>

        example: 

            http://127.0.0.1:5000/seasons/charactersentiment/2/chandler
        
        note: this would return the overall sentiment of all the quotes 
        said by Chandler in season 2 of the Friends TV for show.

### 11 - Endpoint route for sentiment on a given Episode:
Use the number of the season and the number of the episode to identify</br>
the sentiment that the episode has.</br>

        http://127.0.0.1:5000/sentiment/<season>/<episode_number> 

        example: 

            http://127.0.0.1:5000/sentiment/2/2
        
        note: this would return the overall sentiment of episode 2 in season 2
        of all the quotes said during the episode of the Friends TV for show.

### 12 - Endpoint route for posting a new entry through API:
Post a new entry into the DB for future query in API</br>
the sentiment that character during the season.</br>
'{author}', '{episode_number}', '{episode_title}', '{quote}', </br>
'{quote_order}', '{season}')</br>

        http://127.0.0.1:5000/post

______________________________________________________________________
<p align="Left" width="100%">
    <img width="100%" src="https://c.tenor.com/AhORKp-GmwkAAAAC/bye-chandlerbing.gif">
</p>
