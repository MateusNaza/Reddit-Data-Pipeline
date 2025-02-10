import praw
from praw import reddit
import sys

def connect_reddit(client_id, secret_id, user_agent) -> Reddit:
    try:
        reddit = praw.Reddit(client_id=client_id, secret_id=secret_id, user_agent=user_agent)
        print('Conectado ao Reddit!')
        return reddit
    except Exception as e:
        print(e)
        sys.exit(1)

def extract_posts(reddit_instance: Reddit, subreddit: str, time_filter: str, limit=None):
    subreddit = reddit_instance.subreddit(subreddit)
    posts = subreddit.top(time_filter=time_filter, limit=limit)

    posts_list = []

    print(posts)