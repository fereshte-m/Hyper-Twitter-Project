import tweepy
import csv
import twitter_keys

# Important Note!
#
# Please remove / comment above import (twitter_keys)
# and use the following variables in the OAuthHandler and access_token functions
#

# api_key = "YOUR_KEY"
# api_secret = "YOUR_SECRET"
# access_token = "YOUR_ACCESS_TOKEN"
# token_secret = "YOUR_TOKEN_SECRET"

auth = tweepy.OAuthHandler(twitter_keys.consumer_key, twitter_keys.consumer_secret)
auth.set_access_token(twitter_keys.access_key, twitter_keys.access_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

csv_file = open('./MahsaAmini_fetch1.csv', 'a')
csvWriter = csv.writer(csv_file)

search_words = "#MahsaAmini"


def _remove_new_line(line: str):
    return line.replace("\n", "  ")


column_name = ["Username", "Text", "language", "retweet_count", "Time", "location"]
csvWriter.writerow(column_name)

index=0
for tweet in tweepy.Cursor(api.search_tweets, q=search_words, count=5000,
                           since_id=0, tweet_mode='extended').items():
    twt_text = ""
    if hasattr(tweet, "retweeted_status"):
        try:
            twt_text = tweet.retweeted_status.extended_tweet["full_text"]
        except AttributeError:
            twt_text = tweet.retweeted_status.full_text

    else:
        try:
            twt_text = tweet.extended_tweet["full_text"]
        except AttributeError:
            twt_text = tweet.full_text

    csvWriter.writerow(
        [tweet.user.screen_name, _remove_new_line(twt_text), tweet.lang, tweet.retweet_count,
         tweet.created_at, tweet.user.location]
    )
    print("\r", index, end="")
    index += 1
