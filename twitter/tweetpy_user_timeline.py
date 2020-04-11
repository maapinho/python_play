from t import consumer_key,\
    consumer_secret,access_token,\
    acccess_token_secret
import tweepy

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,acccess_token_secret)

twitter=tweepy.API(auth)

public_tweets=twitter.user_timeline(id='appysaudeangola',count=3)
for tweet in public_tweets:
    print('*'*20)
    print(tweet.text)


