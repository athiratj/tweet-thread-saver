import tweepy
import json
import time
import os
from dotenv import load_dotenv
load_dotenv()

# Handles data received from the stream.
class TwitterStreamListener(tweepy.streaming.StreamListener):
    def on_status(self, status):
        result = ('https://twitter.com/twitter/statuses/' + status.in_reply_to_status_id_str)
        api.send_direct_message(status.user.id, result)
        print("Message send!")
        print(status.text)
        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening
    
if __name__ == '__main__':
    listener = TwitterStreamListener()
    
    print('I will now send the Tweets ==>')

    # Authenticate
    auth = tweepy.OAuthHandler(os.getenv("OAuthHandler"), os.getenv("OAuthHandler_2"))
    auth.set_access_token(os.getenv("set_access_token"), os.getenv("set_access_token_2")) 
    api = tweepy.API(auth)

    # Connect the stream to our listener
    stream = tweepy.streaming.Stream(auth, listener)
    x = stream.filter(track=['@getmethread'])
    
    # Timer
    while True:
        time.sleep(15)