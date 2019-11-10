import logging
import tweepy
from config import create_api

api = create_api()

STOP_WORDS = ['game', 'gaming', 'twitch', 'stream', 'streaming',
              'russianfishing4', 'magnetfischen', 'magnetangeln', 'letsplay', 'red dead redemption']

tweet = api.get_status(1192728421983490048,tweet_mode="extended")
if any(s in tweet.full_text.lower().strip() for s in STOP_WORDS):
    print('found by text')
for tag in tweet.entities['hashtags']:
    if tag['text'].lower().strip() in STOP_WORDS:
        print('found by tag')