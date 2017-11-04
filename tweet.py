import tweepy
# from textblob import TextBlob
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer

con_key='qZR2ORc6J26GZHU3SZ7x1wpfI'
con_secret='EsGtDMqS8pKbt2Dp3mxrKLVJUS6BsmnOCc5jki4Qdefv6C2d5X'

access_token = '2610991404-z7CJCyr0eWmpYZ7hZtO4gWmouxBD2DubRANxfMm'
access_token_secret = 'GLyWnhVccs5KUstJ1AXhOrSQ0t2XLjkbWMcIu8mntWlPC'

auth = tweepy.OAuthHandler(con_key, con_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Narendra Modi' + '-filter:links', lang="en", rpp=100)

for tweet in public_tweets:
    print (tweet.text)
    sid = SentimentIntensityAnalyzer()
    text = re.sub(r'@\w+','', tweet.text)
    print (text)
    ss = sid.polarity_scores(text)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]))
        print()
        
# just need to use the compound part        
#         analysis = TextBlob(tweet.text)
#         print (analysis.sentiment.polarity)
