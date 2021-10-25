#!/usr/bin/python3 

#""" Import Libraries"""
from kafka import KafkaConsumer
import sys
from textblob import TextBlob
import pandas as pd 

#""" Kafka broker and tpoic name which produce an consume from it"""
KAFKA_BROKER = 'localhost:9092'
KAFKA_TOPIC = 'tweets'

# Initialize consumer 
consumer = KafkaConsumer (KAFKA_TOPIC, group_id ='group1',bootstrap_servers =
   KAFKA_BROKER)

#-----------------------------------------------------------------------------------
def get_tweet_sentiment(tweet):

  analysis = TextBlob(tweet) #Create a textblob object    
   # """ set sentiment based on Polarity is float which lies in the range of [-1,1] 
   #     where 1 means positive statement and -1 means a negative statement.""" 
  if analysis.sentiment.polarity > 0:	
	  print("positive")        
  elif analysis.sentiment.polarity == 0: 
	  print("neutral")
  else:
	  print("negative")

#""" function to store tweet in list to cand be dealed with pandas"""
def convert(lst):
    try :
    	    return ( str(lst[0]).split())
    except: 
	    return None

for msg in consumer:
  print (msg.value) #print tweet message which is received using kafka consumer 
  list_tweets = convert (msg.value) #store the live tweets in list varaiable
  df=pd.DataFrame(list_tweets) #create dataframe to can apply the sentiment function on each tweet
  df.columns =['tweet'] #create tweet column to can  appliy function  
 #"""Using lambda and passing sentences to sentiment function  """
  df['tweet'].apply(lambda x: (get_tweet_sentiment(' '.join(x))))
  #print(df.head())	


sys.exit()# Terminate the script
