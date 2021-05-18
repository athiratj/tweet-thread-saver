import tweepy
import os
import time
from dotenv import load_dotenv
load_dotenv()

def create_api():
    auth = tweepy.OAuthHandler(os.getenv("OAuthHandler"),
                           os.getenv("OAuthHandler_2"))
    auth.set_access_token(os.getenv("set_access_token"),
                      os.getenv("set_access_token_2"))

    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        print("Error creating API")
        raise e
    return api

api = create_api()
FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)

    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#thorappan' in mention.full_text.lower():
            print('found #thorappan!', flush=True)
            print('responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name +
                    'Yess boss!', mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)
    
