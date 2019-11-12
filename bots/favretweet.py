import logging

import tweepy
from config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

STOP_WORDS = ['game', 'gaming', 'twitch', 'stream', 'streaming', 'survival', 'outdoor',
              'russianfishing4', 'magnetfischen', 'magnetangeln', 'letsplay', 'red dead redemption']


class FavRetweetListener(tweepy.StreamListener):

    def __init__(self, api):
        self.me = api.me()
        self.blocks = api.blocks_ids()
        super(FavRetweetListener, self).__init__(api=api)

    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        # don`t retweet own tweets
        if tweet.in_reply_to_status_id is not None or \
                tweet.user.id == self.me.id or tweet.user.id in self.blocks:
            return
        # don`t retweet if text contains a stop word
        try:
            text = tweet.extended_tweet['full_text']
        except:
            text = tweet.text
        if any(s in text.lower().strip() for s in STOP_WORDS):
            logger.info(f"Tweet id {tweet.id} blocked by text")
            return
        # don`t retweet if tags contqains a stop word
        try:
            hashtags = tweet.extended_tweet['entities']['hashtags']
        except:
            hashtags = tweet.entities['hashtags']
        for tag in hashtags:
            if tag['text'].lower().strip() in STOP_WORDS:
                logger.info(f"Tweet id {tweet.id} blocked by tag")
                return
        try:
            # tweet.favorite()
            tweet.retweet()
        except:
            logger.error("Error on fav and retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)


def main(keywords):
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener, tweet_mode="extended")
    stream.filter(track=keywords, languages=["de"])


if __name__ == "__main__":
    main(["#Angeln", "#Fliegenfischen", "#flytying", "#Fliegenbinden", "#flyfishing"])
