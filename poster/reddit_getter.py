import praw
import random
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="michellejieli/NSFW_text_classifier")
def is_sfw(text):
    return classifier(text)[0]['label'] == 'SFW'

def get_text():
        

    reddit = praw.Reddit(
        client_id='YnYwz0znuWaZz15D3YS-0Q',
        client_secret='__kNNUSuPyQeWn54NSsTmNwX_0GAxw',
        user_agent='Rahu',
        username='The-Meme-Thief6969',
        password='F0otball',
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