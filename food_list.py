import os
import random
import flask
from food_get import food_get
from tweets_get import tweets_get

app = flask.Flask(__name__)
def spoon_url():
    #query = choose
    Tweets = tweets_get()
    print(Tweets[0])

@app.route('/') #python decorator
def index():
    info = tweets_get()
    tweet = random.choice(info[1]) # random choice for refresh tweets
    spoon = random.choice(info[2]) # random choice for refresh spoonacular food
    ingredients = info[3] #len_ingred = random.choice(info[4])
    return flask.render_template(
             "index.html",
             len_tweet = len(tweet),
             len_spoon = len(spoon),
             name = tweet[0],
             screen_name = tweet[1],
             user_id = tweet[2],
             description = tweet[3],
             date = tweet[4],
             link = tweet[5],
             Food_name = info[0],
             recipe_name = spoon[0],
             recipe_url = spoon[1],
             recipe_time = spoon[2],
             recipe_image = spoon[3],
             recipe_source = spoon[4],
             recipe_summary = spoon[5],
             recipe_instructions = spoon[6],
             ingredients = ingredients
             #name = '',
             #screen_name = '',
             #user_id = '',
             #description = '',
             #date = '',
             #link = '',
             #Food_name = '',
             #recipe_name = '',
             #recipe_url = '',
             #recipe_time = '',
             #recipe_image = '',
             #recipe_source = '',
             #recipe_summary = '',
             #recipe_instructions = '',
        )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)
