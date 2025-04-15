import tweepy
import os
import dotenv

dotenv.load_dotenv()
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
bearer_token = os.getenv('BEARER_TOKEN')

def create_tweet(message):
    client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
    api = tweepy.API(auth)

    client.create_tweet(text=message)


if __name__ == "__main__":
    # Twitter message
    twitter_message = 'HHbkmJw49HLJehxPh2M16EFuF5CKFNxY1HeBYNY4pump'

    # Create tweet
    create_tweet(twitter_message)