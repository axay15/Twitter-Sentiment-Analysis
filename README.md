# Twitter-Sentiment-Analysis

------ Siraj Raval's Learn Python for Data Science Part #2 : https://www.youtube.com/watch?v=o_OZdbCzHUA  ------

Sentiment Analysis is understanding and extracting feelings from data.




Steps:
1) Register for Twitter API: 
   Register for Twitter API at https://apps.twitter.com and create an app.

2) Install Dependencies : 1. tweepy (for accessing twitter API), 
                          2. textblob (to help us perform the sentiment analysis), 
                          3. matplotlib (to plot the results) 
                          
   To install the dependencies, run -    
   pip install tweepy   
   pip install textblob   
   pip install matplotlib
   
   
3) Write our script : see demo.py





How does this work:
We split the tweet into words (this process is called tokenization).
Then, we count how many times each words show up, once a text is tokenized.
Then, we check the sentiment value of each word from a sentiment lexicon (it has all the values pre-recorded) to classify the total sentiment value of the tweet.

