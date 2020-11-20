from tweepy import OAuthHandler
from tweepy import API
#from tweepy import Cursor
import tweepy, os, flask, random, datetime, requests, json
from os.path import join, dirname
from dotenv import load_dotenv

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

app = flask.Flask(__name__)

def food_get():
    
    food_list = ["Pork Cutlet", "Bulgogi", "Ramen", "Macaron", "Kimchi", "Sushi", "Chicken Soup", "Udon"]
    # random food choice
    choose = random.choice(food_list)
    return choose

def tweets_get():
    count = 20
    lang = 'en' #I try to search english language
    tweets_list = []
    search = food_get()

    users = api.search_users(search, count)
   #users = api.search(search, count, lang)
    
    # Find spoonacular recipes 
    url = "https://api.spoonacular.com/recipes/complexSearch?apiKey={}&query= {}".format(spoonacular_key, search)
    spoon = []
    response = requests.get(url)
    json_body = response.json()
    recipe_id = json.dumps(json_body['results'][0]["id"])
    id_url =  "https://api.spoonacular.com/recipes/" + str(recipe_id) + "/information?includeNutrition=false&apiKey=" + spoonacular_key
    recipe_response = requests.request("GET", id_url)
    recipe_dictionary = recipe_response.json()
    #print(recipe_dictionary)
    
    # information
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
    
    # ingredients values
    ingredients = []
    
    for item in range(len(recipe_dictionary['extendedIngredients'])):
        ingredients.append(str(recipe_dictionary['extendedIngredients'][item]['originalString']))
        
    print(ingredients)
    print(item)
    #len_ingred = len(ingredients)
    #print(len_ingred)
    spoon.append([recipe_name, recipe_url, recipe_time, recipe_image, recipe_source, 
                   recipe_summary, recipe_instructions])
    
    
    #Twitter user information
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

# Try to use other function    
def spoon_url():
    #query = choose
    Tweets = tweets_get()
    print(Tweets[0])
    return


@app.route('/') #python decorator
def index():
    
    info = tweets_get()
    
    
    tweet = random.choice(info[1]) # random choice for refresh tweets
    spoon = random.choice(info[2]) # random choice for refresh spoonacular food
    ingredients = info[3]
    #len_ingred = random.choice(info[4])
    
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
        )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)
