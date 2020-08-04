# Docker Twitterbot

##### automated retweeting

### How to use?

First, you need an app on [twitter](https://developer.twitter.com/en/apps)

Then create a .env file like this, but with the data you got from twitter. And change STOP_WORDS and HASHTAGS to fit your needs:

    ## Twitter Api
    CONSUMER_KEY=YOUR_CONSUMER_KEY
    CONSUMER_SECRET=YOUR_CONSUMER_SECRET
    ACCESS_TOKEN=YOUR_ACCESS_TOKEN
    ACCESS_TOKEN_SECRET=YOUR_TOEK_SECRET

    ## Bot
    # a comma seperated list of stop words
    # tweets containing one of these words won`t be retweeted
    STOP_WORDS=a,list,of,stopwords

    # a comma seperated list of favorite hashtags
    HASHTAGS=#we,#love,#twitter

### The container

    # pull the container
    docker pull pfitzer/twitterbot
    
    # and run it
    docker run -d --env-file .env --restart always pfitzer/twitterbot
    
### Prerequisites

* Python 3.8
* Tweepy

