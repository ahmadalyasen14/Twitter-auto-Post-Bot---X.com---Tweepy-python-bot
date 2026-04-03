import praw
import tweepy
import os
import random

# ===== Reddit API =====
reddit = praw.Reddit(
    client_id=os.environ['REDDIT_CLIENT_ID'],
    client_secret=os.environ['REDDIT_CLIENT_SECRET'],
    user_agent="bot"
)

# ===== Twitter API =====
client = tweepy.Client(
    consumer_key=os.environ['API_KEY'],
    consumer_secret=os.environ['API_SECRET'],
    access_token=os.environ['ACCESS_TOKEN'],
    access_token_secret=os.environ['ACCESS_TOKEN_SECRET']
)

# ===== Get random post from Reddit =====
subreddit = reddit.subreddit("technology")

posts = list(subreddit.hot(limit=20))
post = random.choice(posts)

tweet = post.title[:280]

# ===== Post tweet =====
client.create_tweet(text=tweet)

print("Tweet posted:", tweet)
