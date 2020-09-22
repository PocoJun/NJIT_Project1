from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import sys, tweepy, os, flask, random, datetime, requests
from os.path import join, dirname
from dotenv import load_dotenv
from ttp import ttp

dotenv_path = join(dirname(__file__), 'food_list.env')
load_dotenv(dotenv_path)

consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

'''
if choose == "Pork cutlet":
    tweets = api.search(choose, count=1, lang='en', exclude='retweets', tweet_mode='extended') 
    #user = api.user_timeline(tweets)
    #print(user)
    tweets.user.screen_name
    print(tweets)
    #for item in tweets:
    #    print(item)
#pork = api.user_timeline("Pork cutlet")
#    url = 'http://search.twitter.com/search.json?q=Pork cutlet'
#    result = requests.get(url)
#    results = result.json()
#    print(results)
'''
food_list = ["Pork cutlet", "Curry", "Ramen", "Cake", "Mashed Potato", "Sushi", "Chicken Soup", "Udon"]

def food_get():
    
    choose = random.choice(food_list)
    return choose


def tweets_get():
    count = 20
    lang = 'en'
    tweets_list = []
    search = food_get()

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

#user_name = tweets_list[0][0]
#user_id = tweets_list[0][1]
#description = tweets_list[0][2]
#date = tweets_list[0][3]

app = flask.Flask(__name__)

@app.route('/') #python decorator
def index():
    
    #tweets = tweepy.Cursor(api.search,  q=search, lang="en", since=date_since).items(5)
    
    #for tweet in tweets:
    #    print(tweet.text)
    
    #result = api.search(q=search, count = 100)
    
    info = tweets_get() 
    tweet = random.choice(info[1]) # random choice for refresh
    
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