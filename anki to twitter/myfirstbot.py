#going to make a twitter bot

import os

import imp
markovbot = imp.load_source('markovbot', '/Users/kylebauder/Desktop/TweetBot/markovbot/markovbot/markovbot27.py')

from markovbot import MarkovBot

# Initialise a MarkovBot instance
tweetbot = MarkovBot()

# Get the current directory's path
dirname = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the book
book = os.path.join(dirname, 'Freud_Dream_Psychology.txt')
# Make your bot read the book!
tweetbot.read(book)

#
my_first_text = tweetbot.generate_text(25, seedword=['dream', 'psychoanalysis'])
print("tweetbot says:")
print(my_first_text)

# ALL YOUR SECRET STUFF!
# Consumer Key (API Key)
cons_key = 'Y7dzXbP9Jx7HPnLyscaAcuzHD'
# Consumer Secret (API Secret)
cons_secret = 'OE9tDUnQLzJGZ6LcwliVt5OJ3M3u8Xdx21ETSJMQtaRT0qe9qA'
# Access Token
access_token = '953403732384886784-A4eYTNV8nfb8meOEoN0zbQvvchi0Agr'
# Access Token Secret
access_token_secret = 'jfm2s1wkORCc1HgGyCV28c7pRnMuGAzU4TvLgz0QOpTDR'

# Log in to Twitter
tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)

# Start periodically tweeting
tweetbot.twitter_tweeting_start(days=0, hours=19, minutes=30, keywords=None, prefix=None, suffix='#N64 German')

# Use the following to stop periodically tweeting
# (Don't do this directly after starting it, or your bot will do nothing!)

import time; time.sleep(86400)

tweetbot.twitter_tweeting_stop()
