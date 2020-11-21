from os.path import join, dirname
import json
import os
from dotenv import load_dotenv
import requests
from tweepy import OAuthHandler
from tweepy import API
from food_get import food_get

# spoon env secret key
dotenv_path = join(dirname(__file__), 'spoon.env')
load_dotenv(dotenv_path)

# twitter env secret kegity
dotenv_path = join(dirname(__file__), 'food_list.env')
load_dotenv(dotenv_path)

consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

spoonacular_key=os.getenv('SPOONACULAR_KEY')
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

def tweets_get():
    count = 20
    tweets_list = []
    search = food_get()
    users = api.search_users(search, count) #users = api.search(search, count, lang)
    url = "https://api.spoonacular.com/recipes/complexSearch?apiKey={}&query= {}".format(spoonacular_key, search)
    spoon = []
    response = requests.get(url)
    json_body = response.json()
    recipe_id = json.dumps(json_body['results'][0]["id"])
    id_url =  "https://api.spoonacular.com/recipes/" + str(recipe_id) + "/information?includeNutrition=false&apiKey=" + spoonacular_key
    recipe_response = requests.request("GET", id_url)
    recipe_dictionary = recipe_response.json() #print(recipe_dictionary)
    if url:
        recipe_name = recipe_dictionary["title"]
        recipe_url = recipe_dictionary["sourceUrl"]
        recipe_time = recipe_dictionary["readyInMinutes"]
        recipe_image = recipe_dictionary["image"]
        recipe_source = recipe_dictionary["servings"]
        #recipe_score = recipe_dictionary["spoonacularScore"]
        #recipe_likes = recipe_dictionary["aggregateLikes"]
        recipe_summary = recipe_dictionary["summary"]
        recipe_instructions = recipe_dictionary["instructions"]
        #recipe_ingredients = recipe_dictionary["ingredients"]
    else:
        recipe_name = ''
        recipe_url = ''
        recipe_time = ''
        recipe_image = ''
        recipe_source = ''
        recipe_summary = ''
        recipe_instructions = ''
    ingredients = [] # ingredients values
    for item in range(len(recipe_dictionary['extendedIngredients'])):
        ingredients.append(str(recipe_dictionary['extendedIngredients'][item]['originalString']))
    print(ingredients)
    print(item)
    #len_ingred = len(ingredients)
    #print(len_ingred)
    spoon.append([recipe_name, recipe_url, recipe_time, recipe_image, 
    recipe_source, recipe_summary, recipe_instructions])
    for tweets in users:
        name= tweets.name
        screen_name = tweets.screen_name
        user_id = tweets.id
        description = tweets.description
        date = tweets.created_at
        link = tweets.url
        tweets_list.append([name, screen_name, user_id, description, date, link])
    tweet_information = [search, tweets_list, spoon, ingredients]
    return tweet_information