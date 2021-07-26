import tweepy

# for this to work need info from twitter api account app details
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

for follower in tweepy.Cursor(api.followers).items():
    print(follower.name)