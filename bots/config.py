import tweepy
import logging
import os

CONSUMER_KEY = 'zzQJaeuapsfDWQuoj7rA'
CONSUMER_SECRET = 'VOmmYerDc89sswQmMJa0C83nFa1EsLn1aGQ5H7uvoQ'
ACCESS_TOKEN = '980216408-re4MRB6YNkjcVSwy8Ykh8E8rHNgi1vYl7LUkjkOg'
ACCESS_TOKEN_SECRET = 'FdWFpn93T5YxaPrccI7rkFzpfvpb9C3Hq99oCfcJi4'

logger = logging.getLogger()


def create_api():
    consumer_key = CONSUMER_KEY
    consumer_secret = CONSUMER_SECRET
    access_token = ACCESS_TOKEN
    access_token_secret = ACCESS_TOKEN_SECRET

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
