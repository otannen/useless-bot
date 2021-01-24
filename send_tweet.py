import tweepy

from gather_data import Tweet
from creds import auth

api = tweepy.API(auth)
today = Tweet("Chicago")

decision = """Stay inside and read the news.
If the news is too depressing read the wikipedia article instead."""
if today.get_weather() >= 32:
    decision = "Based on these conditions you should go outside."


status = """Owen, today's max temp is %d degrees.
A gallon of gas is $%.2f.
Today's top news story: %s 
Here's a random wikipedia article: %s

%s
 
""" % (
    today.get_weather(),
    today.get_gas_price(),
    today.get_news(),
    today.get_wiki(),
    decision,
)

api.update_status(status)
