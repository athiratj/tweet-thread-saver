# Import tweepy Package
import tweepy
import logging
import time
from credentials import *
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Set the authentication credentials
def create_api():
    auth = tweepy.OAuthHandler(OAuthHandler, OAuthHandler_2)
    auth.set_access_token(set_access_token, set_access_token_2)
    # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        print("Error creating API")
        raise e
    return api

# Use the api object to call the Twitter API
def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            if any(keyword in tweet.text.lower() for keyword in keywords):
                logger.info(f"Messaging to {tweet.user.name}")
                result = ('https://twitter.com/twitter/statuses/' + tweet.in_reply_to_status_id_str)
                api.send_direct_message(tweet.user.id, result)
                print(tweet.text)
                if not tweet.favorited:
                    try:
                        tweet.favorite()
                    except Exception as e:
                        logger.error("Error on favorite", exc_info=True)
        else:
            reply_status="No tweet available to save."
            api.update_status(status=reply_status, in_reply_to_status=tweet.id)
            api.send_direct_message(tweet.user.id,reply_status)          

    return new_since_id

def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, ["@getmethistweet"], since_id)
        logger.info("Waiting...")
        time.sleep(5)

if __name__ == "__main__":
    main()
