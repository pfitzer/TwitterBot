# Docker Twitterbot

[<img src="https://github.com/pfitzer/TwitterBot/workflows/Create%20Release/badge.svg">](https://github.com/pfitzer/TwitterBot/actions?query=workflow%3A%22Create+Release%22)
[<img src="https://img.shields.io/docker/pulls/pfitzer/twitterbot.svg?style=flat-square&logo=docker">](https://hub.docker.com/r/pfitzer/twitterbot)
[<img src="https://pyup.io/repos/github/pfitzer/TwitterBot/shield.svg?t=1605168945323">](https://pyup.io/account/repos/github/pfitzer/TwitterBot/)
[<img src="https://pyup.io/repos/github/pfitzer/TwitterBot/python-3-shield.svg?t=1605168967691">](https://pyup.io/account/repos/github/pfitzer/TwitterBot/)

##### automated retweeting

### How to use?

First, you need to create an app on [twitter](https://developer.twitter.com/en/apps)

Then create a .env file with the following content and add the data you got from twitter.
And change STOP_WORDS and HASHTAGS to fit your needs.

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
    
    # a list of preferred languages
    TWITTER_LANG=en,de

### The container

    # pull the container
    docker pull pfitzer/twitterbot
    
    # and run it
    docker run -d --env-file .env --restart always pfitzer/twitterbot
    
### Build from scratch
    
    git clone https://github.com/pfitzer/TwitterBot.git
    cd TwitterBot
    docker build . -t twitterbot
    
### Enhanced functionality

There are two more python files under the bots directory

* autoreply.py is for auto reply to messages
* followfollowers.py is for automatic re-follow

To use these functions, add them as CMD to the dockerfile and build the image from scratch.
    
### Prerequisites

* Python 3.8
* Tweepy

