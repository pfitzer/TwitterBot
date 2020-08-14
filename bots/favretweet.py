import logging
import time

import tweepy
from config import create_api, Config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


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
        except (ValueError, AttributeError):
            text = tweet.text
        if any(s in text.lower().strip() for s in Config.get_stop_words()):
            logger.info(f"Tweet id {tweet.id} blocked by text")
            return
        # don`t retweet if tags contain a stop word
        try:
            hashtags = tweet.extended_tweet['entities']['hashtags']
        except (ValueError, AttributeError):
            hashtags = tweet.entities['hashtags']
        for tag in hashtags:
            if tag['text'].lower().strip() in Config.get_stop_words():
                logger.info(f"Tweet id {tweet.id} blocked by tag")
                return

        tweet.retweet()
        return

    def on_error(self, status):
        logger.error(status)
        if status == 420:
            time.sleep(15 * 60)
        return False

    def on_connect(self):
        logger.info("You are connected to the streaming server.")
        return

    def on_exception(self, exception):
        logger.error(exception)
        return


def main():
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener, tweet_mode="extended")
    stream.filter(track=Config.get_hashtags(), languages=Config.get_language())


if __name__ == "__main__":
    main()
