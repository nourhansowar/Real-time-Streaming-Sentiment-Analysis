"""
Arpproach 1 is to get live stream of tweets
"""
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

ACCESS_TOKEN = "1438229384037609472-xSWm7vR3s0BHmNesJmqyj6F7QhXUL6"
ACCESS_TOKEN_SECRET = "qt6lhE9syMKPfMhQJIWvOpKloo7hWZ20TaCKPcCeql6OO"
CONSUMER_KEY = "xPhOYcGH2TkLla7KzGr5ftEHn"
CONSUMER_SECRET = "2jocMtXHiDxd4FPLyKpyTgk4fRvU6BVnT2qrR0FUywmRnZboF3"

"""
using tweepy library to deal with twitter

"""
# # # # TWITTER STREAMER # # # #

"""
   Class for streaming and processing live tweets.
"""
class TwitterStreamer():

    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):

        listener = StdOutListener(fetched_tweets_filename)

        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

        stream = Stream(auth, listener)
        # This line filter Twitter Streams to capture data by the keywords:
        stream.filter(track=hash_tag_list)
        #preprocessing(stream.filter(track=hash_tag_list))



# # # # TWITTER STREAM LISTENER # # # #
"""
    This is a basic listener that just prints received tweets to stdout.
"""
class StdOutListener(StreamListener):

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    hash_tag_list = ["Pizaa"]
    fetched_tweets_filename = "tweets.txt"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)


