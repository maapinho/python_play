from t import consumer_key,\
    consumer_secret,access_token,\
    acccess_token_secret
import tweepy

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,acccess_token_secret)

twitter=tweepy.API(auth)

tweet=twitter.update_status('This is my first ever\
    automated tweet. I am taking my own job away \
        @tweepy @vscode #python 2')
