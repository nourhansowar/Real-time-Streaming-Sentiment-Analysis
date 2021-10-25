# Real-time-Streaming-Sentiment-Analysis

Big data trend has enforced the data-centric systems to have continuous fast data streams.  In  recent  years,  real-time analytics on stream data has formed into a  new research field, which aims to answer queries about  “what-is-happening-now” with  a  negligible  delay.  The real challenge with real-time stream data processing is that it is impossible to store instances of data, and therefore online analytical algorithms are utilized. To  perform  real-time  analytics,  pre-processing of data should be performed in a  way that only a  short summary of the stream is stored in main memory. In addition, due to high speed of arrival, the average processing time for each instance of data should be in such a  way that incoming instances are not lost without being captured.  

## Architecture:
![image](https://user-images.githubusercontent.com/48545560/138675969-545bcb1e-7f49-4902-91f2-9e48b4a21f54.png)

## Methodologies :

1- Get live Stream of tweets from Twitter API:

First of all, I have submitted an application for twitter developer to use twitter API. Then, once it has been approved, I have created an APP to get credentials from the Development Portal (consumer_key, consumer_secret_key,Access_token,Access_token_secret).

Second, using pycharm on windows , I have installed a tweepy library for connecting and getting the tweets from the Twitter API. 
Then, With a simple script, I can get a live stream of tweets using a specific keyword which initialized  in code : Basic_Code
2-  Kafka Stage & Its environment :

At this stage, I take the time to understand what kafka is, how it works, and why I need it. Kafka is a distributed publish-subscribe messaging system that maintains feeds of messages in partitioned and replicated topics. 

There are three players in the Kafka ecosystem: producers, topics (run by brokers) and consumers.


