import os
import pickle
import sys

import numpy as np
import tweepy
from config import create_api

PICKLE_FILE = os.path.join(os.path.abspath(__file__), 'tweets.pkl')

api = create_api()
data_set = {}


for tweet in tweepy.Cursor(api.search,q="#angeln",count=10000,
                           lang="de",
                           since="2016-01-01").items():
    for reply in tweepy.Cursor(api.search, q='to:' + tweet.user.name, since_id=tweet.id,  result_type='recent', timeout=999999).items(100):
        if hasattr(reply, 'in_reply_to_status_id_str'):
            if (reply.in_reply_to_status_id_str == tweet.id):
                if not tweet.id in data_set:
                    data_set[tweet.id] = {'tweet': tweet.text, 'replies': [reply.text]}
                else:
                    data_set[tweet.id]['replies'].append(reply.text)
pickle.dump(np.array(data_set), open(PICKLE_FILE, 'w'))
sys.exit(0)