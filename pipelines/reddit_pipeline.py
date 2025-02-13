import pandas as pd

from etls.reddit_etl import connect_reddit, extract_posts, transform_data
from utils.constants import CLIENT_ID, SECRET, OUTPUT_PATH, USER_AGENT


def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):

    # Conecta a uma instancia do Reddit
    instance = connect_reddit(CLIENT_ID, SECRET, USER_AGENT)

    # Extrai os posts
    posts = extract_posts(instance, subreddit, time_filter, limit)

    # transforma os dados
    post_df = transform_data(posts)

    print(post_df.head())
    