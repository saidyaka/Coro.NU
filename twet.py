import sys
from twython import Twython

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

 

def tweetIt(sti):
    api = Twython(consumer_key, consumer_secret, access_token, access_token_secret)


    message = sti
    api.update_status(status= message)
    print("Tweeted: \n"+sti)

