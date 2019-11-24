# Docker Twitterbot

##### automated retweeting

How to use?


    cp .env.example .env
    # edit the .env file to fit your needs
    
    # build the docker image
    docker build . -t twitterbot 
    
    # the container
    docker run -d --env-file .env --restart always twitterbot

