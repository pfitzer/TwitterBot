import logging
import tweepy
from config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

STOP_WORDS = ['game', 'gaming', 'twitch', 'stream', 'streaming',
              'RussianFishing4', 'Magnetfischen', 'Magnetangeln', 'letsplay', 'red dead redemption']


class FavRetweetListener(tweepy.StreamListener):
    
    def __init__(self, api):
        self.me = api.me()
        super(FavRetweetListener, self).__init__(api=api)

    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        # don`t retweet own tweets
        if tweet.in_reply_to_status_id is not None or \
                tweet.user.id == self.me.id:
            return
        # don`t retweet if text contqains a stop word
        if any(s in tweet.text.lower().strip() for s in STOP_WORDS):
            return
        # don`t retweet if tags contqains a stop word
        for tag in tweet.entities['hashtags']:
            if tag['text'] in STOP_WORDS:
                return
        try:
            # tweet.favorite()
            tweet.retweet()
        except Exception as e:
            logger.error("Error on fav and retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)


def main(keywords):
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["de"])


if __name__ == "__main__":
    main(["#Angeln", "#Fliegenfischen", "#flytying", "#Fliegenbinden", "#flyfishing"])
