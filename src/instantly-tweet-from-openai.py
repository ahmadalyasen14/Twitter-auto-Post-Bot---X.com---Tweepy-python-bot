import feedparser
import tweepy
import os
import random

# ===== Twitter API =====
client = tweepy.Client(
    consumer_key=os.environ['API_KEY'],
    consumer_secret=os.environ['API_SECRET'],
    access_token=os.environ['ACCESS_TOKEN'],
    access_token_secret=os.environ['ACCESS_TOKEN_SECRET']
)

# ===== Reddit RSS Feed =====
RSS_URL = "https://www.reddit.com/r/technology/.rss"

feed = feedparser.parse(RSS_URL)
entries = feed.entries

# اختار منشور عشوائي
post = random.choice(entries)

tweet = post.title[:280]  # خذ العنوان فقط

# ===== نشر التغريدة =====
client.create_tweet(text=tweet)

print("Tweet posted:", tweet)
