from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import sys, tweepy, os, flask, random, datetime, requests, json
from os.path import join, dirname
from dotenv import load_dotenv
from ttp import ttp

dotenv_path = join(dirname(__file__), 'food_list.env')
load_dotenv(dotenv_path)

dotenv_path = join(dirname(__file__), 'spoon.env')
load_dotenv(dotenv_path)

consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

spoonacular_key=os.getenv('SPOONACULAR_KEY')

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

food_list = ["Pork Cutlet", "Curry", "Ramen", "Cake", "Mashed Potato", "Sushi", "Chicken Soup", "Udon"]

app = flask.Flask(__name__)

#def food_get():
    
choose = random.choice(food_list)
    #return choose


def tweets_get():
    count = 20
    lang = 'en'
    tweets_list = []
    search = choose

    users = api.search_users(search, count, lang)

    for item in users:
        name= item.name
        screen_name = item.screen_name
        user_id = item.id
        description = item.description
        date = item.created_at
        link = item.url
        
        tweets_list.append([name, screen_name, user_id, description, date, link])
    
    tweet_information = [search, tweets_list]
    return tweet_information

def spoon_url():
    query = choose
    url = "https://api.spoonacular.com/recipes/complexSearch?apiKey={}&query= {}".format(spoonacular_key, query)
    response = requests.get(url)
    print(response)
    return url

def food_recipe():
    #search = food_get()
    #link = "https://api.spoonacular.com/recipes/{}/information?apiKey={}".format(search, spoonacular_key)
    spoon = spoon_url()
    
    return spoon


@app.route('/') #python decorator
def index():
    
    info = tweets_get()
    spoon = spoon_url()
    print(spoon)
    response = requests.get(spoon)
    #print(response)
    json_body = response.json()
    #print(json_body)
    print(json.dumps(json_body['results'][0]["id"]))
    print(json.dumps(json_body['results'][0]["title"]))
    print(json.dumps(json_body['results'][0]["image"]))
    
    tweet = random.choice(info[1]) # random choice for refresh
    
    #recipe = food_recipe()
    #print(recipe)
    
    return flask.render_template(
             "index.html",
             len_tweet = len(tweet),
             name = tweet[0],
             screen_name = tweet[1],
             user_id = tweet[2],
             description = tweet[3],
             date = tweet[4],
             link = tweet[5],
             Food_name = info[0]
        )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)