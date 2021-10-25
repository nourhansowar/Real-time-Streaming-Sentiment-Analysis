#!/usr/bin/python3 

#""" Import Libraries"""
from kafka import KafkaProducer
import tweepy 
import sys
import re

# put project API keys on Twitter Developer
consumer_key = "gcOqqLnAfqyiCKFM94mmJ5yNW"
consumer_secret_key = "0B24bPCkERpiLCtDFbbHGXhQlsR4vmYqn7uA9js6mqqkFb4UMv"
access_token = "1438229384037609472-m16AbLG9Wf0pHsRjPCo3qFsh4Kz6FY"
access_token_secret = "ImiGL344FJ0lBPrdRg4YCISGyHble4gem0ipLHdKZfO10"

#"""The keyword which we need to search on it in twitter"""
TWEET_TOPICS = ['pizza']

#""" Kafka broker and tpoic name which produce an consume from it
KAFKA_BROKER = 'localhost:9092'
KAFKA_TOPIC = 'tweets'

#----------------------------------------------------------------------
#""" Create Listner Class to  """
class StdOutListener (tweepy.StreamListener):
    def on_error(self, status_code):
        if status_code == 402:
            return False

    def on_status(self, status):
        tweet = status.text
	
	#simple regular expression 
        tweet = re.sub(r'RT\s@\w*:\s', '', tweet)
        tweet = re.sub(r'https?.*', '', tweet)

	#"""send live tweet to kafka topic which is named (tweets) """
        global producer
        producer.send(KAFKA_TOPIC, bytes(tweet, encoding='utf-8'))

        print (tweet) #print live tweets on terminal
#-------------------------------------------------------------------------

listener = StdOutListener() # create object listener

#Authentication with Twitter Developer App         
auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)

stream = tweepy.Stream(auth, listener) #get stream using Stream method creted in tweepy module

try:
    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)#create kafka Producer on kafka broker
    print(producer)
except Exception as e:
    print(f'Error Connecting to Kafka --> {e}')
    sys.exit(1)
# Filter Twitter Streams to capture data by the keywords:
stream.filter(track=TWEET_TOPICS)        

