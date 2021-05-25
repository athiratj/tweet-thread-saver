 ![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)
# GET ME TWEET APP
### Meet the bot [@getmethistweet](https://twitter.com/getmethistweet).
It uses the Twitter API to to help you save threads more easily. Just tag the bot as reply to the tweet which u need it to direct message. This project is awesome...

## Team members
1. [Sangeetha D](https://github.com/SANGEETHA-gli)
2. [Syamili S](https://github.com/syamiliwayanad2001)
3. [Athira T J](https://github.com/athiratj)

## Team Id
BFH/reciJV3XlF0HW5cly/2021

## Link to product walkthrough
[link to video]

## How it Works ?

* Get Me Tweet App is a Twitter bot which save the tweets in the Inbox as direct messages. 
  1. The Massage settings in Twitter should be changed before using the bot.
  2. The user has to just tag the bot as a reply to the tweet which the user would like to save for later reference.The bot also favourites the user's tweet.

**[Product Video](https://www.loom.com/share/de30830732464a328426a664890ea955)**
## Libraries used
Tweepy - 3.10.0

## How to configure
#### What You Need:
-   [Tweepy](http://www.tweepy.org/), an easy-to-use Python library for accessing the **Twitter API**.
-	Make a [Twitter Developer Account](https://developer.twitter.com/en) and make sure you fully understand  [Twitter's Rules on Automation](https://support.twitter.com/articles/76915)!
- You need to have a [Heroku Account](https://dashboard.heroku.com/).
#### Instructions:
-   The first step is to clone this repository which will contain the bot files and then create a  virtual environment:
     ``` bash
      $ git clone https://github.com/athiratj/tweet-thread-saver.git
      $ cd tweet-thread-saver
      $ python3 -m venv venv 
      ```
-   Activate the newly created virtual environment and then use pip to install Tweepy package:
     ``` bash
      $ source venv/bin/activate
      $ pip install tweepy
      ```
-   Create a new  [**Twitter Application**](https://apps.twitter.com/app/new). This is where you'll generate your keys, tokens, and secrets.
-   Fill in your keys, tokens, and secrets in the **credentials.py** file:
    ```
    OAuthHandler='CONSUMER_KEY'
    OAuthHandler_2='CONSUMER_SECRET'
    set_access_token='ACCESS_TOKEN'
    set_access_token_2='ACCESS_TOKEN_SECRET'
    ```
## How to Run

-   Run the **getmethistweet.py** script using command	`python3 givemethistweet.py`

#### Deployment on Heroku:
-	If the script runs without any errors it can be deployed on [**Heroku**](https://dashboard.heroku.com/).
-	Once deployment is done your Twitter bot is good to go!:sunglasses:
