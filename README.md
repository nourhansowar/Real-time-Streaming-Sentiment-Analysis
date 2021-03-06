# Real-time-Streaming-Sentiment-Analysis

Big data trend has enforced the data-centric systems to have continuous fast data streams.  In  recent  years,  real-time analytics on stream data has formed into a  new research field, which aims to answer queries about  “what-is-happening-now” with  a  negligible  delay.  The real challenge with real-time stream data processing is that it is impossible to store instances of data, and therefore online analytical algorithms are utilized. To  perform  real-time  analytics,  pre-processing of data should be performed in a  way that only a  short summary of the stream is stored in main memory. In addition, due to high speed of arrival, the average processing time for each instance of data should be in such a  way that incoming instances are not lost without being captured.  

## Architecture:
![image](https://user-images.githubusercontent.com/48545560/138675969-545bcb1e-7f49-4902-91f2-9e48b4a21f54.png)

## Methodologies :

## >> 1- Get live Stream of tweets from Twitter API:

First of all, I have submitted an application for twitter developer to use twitter API. Then, once it has been approved, I have created an APP to get credentials from the Development Portal (consumer_key, consumer_secret_key,Access_token,Access_token_secret).

Second, using pycharm on windows , I have installed a tweepy library for connecting and getting the tweets from the Twitter API. 
Then, With a simple script, I can get a live stream of tweets using a specific keyword which initialized  in code : Basic_Code * Check codes* 
## >> 2-  Kafka Stage & Its environment :

At this stage, I take the time to understand what kafka is, how it works, and why I need it. Kafka is a distributed publish-subscribe messaging system that maintains feeds of messages in partitioned and replicated topics. 

There are three players in the Kafka ecosystem: producers, topics (run by brokers) and consumers.
![image](https://user-images.githubusercontent.com/48545560/138676116-80e1a12a-34d8-4616-8ed3-05c801e3b7a9.png)

 * start a Zookeeper instance, create a Kafka broker, and publish/subscribe to topics in kafka directory.* 

![image](https://user-images.githubusercontent.com/48545560/138676262-cd3e512d-4562-41c5-9b2e-3b353885d92f.png)


## >> 3- Send live stream using kafka producer and kafka consumer:

In this approach, I ‘ve developed 2 scripts : one for Producers produce messages to a topic and another for Consumers read the messages of a set of partitions of a topic from the broker.Kafka Producer Script  Kafka Consumer Script 
![image](https://user-images.githubusercontent.com/48545560/138676889-d9528f84-24bc-45a7-aa50-6fd41bdf28ee.png)


## ** Future Enhancements

1- Spark: 
This is one of the first future enhancements I will do in the prolect.

2- Get Flexibility for user to enter the keyword which he want to search on: 
By implementing a simple web script using html to take the keyword from the user.


## ** Technologies used
Pycharm
Ubuntu18
Tweepy
Kafka
Zookeeper
pandas


