import tweepy
import logging
import os
import sys

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

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


class Config(object):

    @staticmethod
    def get_stop_words():
        try:
            stop_words = os.environ['STOP_WORDS'].split(',')
        except ValueError:
            stop_words = []
        return stop_words

    @staticmethod
    def get_hashtags():
        try:
            return os.environ['HASHTAGS'].split(',')
        except ValueError:
            logger.error('No HASHTAGS environment variable is set. I stop now.')
            sys.exit(1)

    @staticmethod
    def get_language():
        try:
            twitter_lang = os.environ['TWITTER_LANG'].split(',')
        except ValueError:
            twitter_lang = ['en']
        return twitter_lang
