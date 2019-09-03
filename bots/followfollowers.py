import tweepy
from tweepy.error import TweepError
import logging
from bots.config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            try:
                logger.info(f"Following {follower.name}")
                follower.follow()
            except TweepError as e:
                logger.error(e.reason)
                if e.api_code == 161:
                    time.sleep(600)
                continue


def main():
    api = create_api()
    while True:
        follow_followers(api)
        logger.info("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()
