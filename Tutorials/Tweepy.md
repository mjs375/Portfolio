# TWEEPY: Twitter Bot in Python
- Automatically post tweets, follow followers, retweet, reply to mentions, &c.

### Send a Tweet with ```Tweepy```
- **Basic Steps for all Tweepy Programs**:
  - 1. Import ```tweepy``` package
  - 2. Set authentication credentials
  - 3. Create a new ```tweepy.api``` object
  - 4. Use the ```api``` object for call the Twitter API
```python
import tweepy # 

 # Authenticate to Twitter
 auth = tweepy.OAuthHandler("CONSUMER_KEY","CONSUMER_SECRET")
 auth.set_access_token("ACCESS_TOKEN","ACCESS_TOKEN_SECRET")
 
 # Create API object
 api = tweepy.API(auth)
 
 # Create a Tweet
 api.update_status("Hello Tweepy")
 ```
 
 ### TWITTER API
 - Twitter's API lets developers access most of Twitter's functionality: read and write information related to Twitter entities such as tweets, users, and trends (and more: likes, DMs, media...)
  - **```OAth```**: commonly-used open authorization protocol, used to authenticate each request.
- Different kinds fo automations: *bots, analytics, tools...*
  - Restrictions: *rate limits, spamming, misleading users, &c.*
    - Rate Limits: *if you exceed rate limits, you'll be locked out for 5-15 minutes... careful!*
 
 ### Installing Tweepy
 - **Tweepy**: an open-source Python package that gives an easy way to access Twitter API.
   - First, create a project folder, and then create a virtual environment.
```shell
$ mkdir tweepy-bots # make directory
$ cd tweepy-bots # change directory
$ python3 -m venv env # create virtual environment
$ source env/bin/activate # activate venv
$ pip install tweepy # install Tweepy
$ pip freeze > requirements.txt # create a requirements.txt, putting all dependencies in the venv inside
```

### Twitter API Authentication Credentials
- Twitter API needs 4 things (text strings):
  – ```Consumer key```, ```Consumer secret```
  - ```Access token```, ```access secret```
- 1. Create a Twitter Account, then go to the [Twitter developer site](https://developer.twitter.com/). Twitter grants API access to *apps*, not accounts. Create an application for a developer account.

WAITING ON TWITTER DEVELOPER APPROVAL...

















Source: [Real Python](https://realpython.com/twitter-bot-python-tweepy/#installation)
