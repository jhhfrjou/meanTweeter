import twitter
import json

phrasefile = json.load(open('phrases.json'))
phrases = phrasefile['phrases']

secrets = json.load(open('secrets.json'))
api = twitter.Api(consumer_key=secrets['consumer_key'],
                  consumer_secret=secrets['consumer_secret'],
                  access_token_key=secrets['access_token_key'],
                  access_token_secret=secrets['access_token_secret'])