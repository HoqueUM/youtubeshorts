import praw
import random
from transformers import pipeline
from dotenv import load_dotenv
import os

load_dotenv()

classifier = pipeline("sentiment-analysis", model="michellejieli/NSFW_text_classifier")
def is_sfw(text):
    return classifier(text)[0]['label'] == 'SFW'

def get_text():
        

    reddit = praw.Reddit(
        client_id=os.getenv('CLIENT_ID'),
        client_secret=os.getenv('CLIENT_SECRET'),
        user_agent=os.getenv('USER_AGENT'),
        username=os.getenv('USERNAME'),
        password=os.getenv('PASSWORD'),
    )

    subreddits = ['confession']
    selected_subreddit = random.choice(subreddits)
    subreddit = list(reddit.subreddit(selected_subreddit).top('week', limit=99))

    selected_post = None
    while not selected_post:
        post = random.choice(subreddit)
        if is_sfw(post.title):
            selected_post = post

    text = selected_post.title + selected_post.selftext[:1000]
    return text, post.title