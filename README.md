# project1-cl678 (Changjun Lee)
# CS490-005section
# Detailed instructions on how to get this running!
# Step to deploy the app

1. Sign up for the twitter developer portal at https://developer.twitter.com
2. Navigate to https://developer.twitter.com/en/portal/projects-and-apps and make a new app.
3. Click on the key symbol after creating your project, and it will take you to your keys and tokens.
   create file.env for security
4. Run the following in your terminal: sudo pip install tweepy (or) sudo pip3 install tweepy (or) pip install tweepy (or) pip3 install tweepy
   sudo pip install tweepy(window), 
   sudo pip install flask
   sudo pip install python-dotenv
5. Add your secret keys by making file.env

    KEY=''
    
    KEY_SECRET=''
    
    TOKEN=''
    
    TOKEN_SECRET=''
 
    TODO use environment variables in lieu of the hardcorded Twitter.
6. Run python file.py Make sure you add the secret keys as environment variables or store in your env file.
# Run on Heroku
1. Sign up for heroku at heroku.com
2. Install heroku by running npm install -g heroku
3. Following steps: 
   * heroku login -i  
   * heroku create  
   * git push heroku master
4. Check out git remote -v that you add heroku
5. Navigate Heroku website
6. Add your secret keys (from tweepy.env) by going to https://dashboard.heroku.com/apps and clicking into your app.
   Add your secret keys (from step 2) by making a new root-level file called tweepy.env and populating it as follows.
    KEY=''
    KEY_SECRET=''
    TOKEN=''
    TOKEN_SECRET=''
    and check out put spoonacular key if you have!!!
7. Configure requirements.txt with all requirements needed to run your app.
8. Configure Procfile with the command needed to run your app.
9. If you are still having issues, you may use heroku logs --tail

#Technical issues that you experienced during the project1

1. flask website refresh and reload wouldn't work, so I searched google and other url websites how to solve the problem.
2. I found out html refreshing in time limit, thereby I made the website automatically refresh.
3. I created Heroku and login to connect the app. It was not work I don't why. As a result, Heroku error H-10 APP error, and I found out not using import in python file.

# Problems

1. I think my coding looks dirty, so I need to organize the functions.
2. In twitter user, I need to change search_user to search to find language= 'en'.
3. The size of picture from spoonacular does not fit the box. If I have more time, I can fix it.



