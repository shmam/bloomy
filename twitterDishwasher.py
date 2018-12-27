import tweepy

# Private credentials for your app obtained after creating 
# your app on https://developer.twitter.com 
api_key = '...'
api_secret = '...'
access_token = '...'
access_token_secret = '...'

# OAuth steps 
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

your_tweet = "your tweet goes here"

api.update_status(your_tweet)