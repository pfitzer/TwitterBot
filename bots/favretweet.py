import logging

import tweepy
from config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class FavRetweetListener(tweepy.StreamListener):
    
    def __init__(self, api):
        self.me = api.me()
        super(FavRetweetListener, self).__init__(api=api)

    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
                tweet.user.id == self.me.id:
            return
        try:
            tweet.favorite()
            tweet.retweet()
        except Exception as e:
            logger.error("Error on fav and retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)


def main(keywords):
    keys = []
    for key in keywords:
        keys.append(key + " -filter:retweets")
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keys, languages=["de"])


if __name__ == "__main__":
    main(["#Angeln", "#Fliegenfischen", "#Flytying", "#Fliegenbinden"])
