from textblob import TextBlob
import tweepy
import matplotlib.pyplot as plt

# we need 4 variables to authenticate with twitter
# you'll find values for these 4 variables in your twitter app dashboard:
 
consumer_key = 'Enter consumer key here'
consumer_secret = 'Enter consumer secret'


access_token = 'Enter access token'
access_token_secret = 'Enter access token secret'


# Authenticate or login via code:
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)   # our main variable

# we'll now search and collect tweets with a certain keyword:

topic = input("What topic do you want to search?")
no_of_tweets = int(input("how many tweets do you want to search?"))


public_tweets = api.search(topic, count = no_of_tweets)

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    
# the above print statement returns polarity and subjectivity
# polarity measures how negative or positive the text is
# subjectivity measures how much of an opinion it is versus how factual

# Next, we'll plot the reaction of the people as +ve, -ve or neutral on a pie chart

polarity = 0
positive = 0
negative = 0
neutral = 0 

for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity
    
    if (analysis.sentiment.polarity == 0): # neutral tweet
        neutral += 1
    elif (analysis.sentiment.polarity > 0): # positive tweet
        positive += 1
    elif (analysis.sentiment.polarity < 0): # negative tweet
        negative += 1
        

# Calculating average of people's reaction
avg_polarity = polarity/no_of_tweets

if (avg_polarity == 0):
    avg_reaction = "Neutral"
elif (avg_polarity > 0):
    avg_reaction = "Positive"
elif (avg_polarity < 0):
    avg_reaction = "Negative"
    
print("Average Polarity = " + str(avg_polarity))
print("Based on analysis of "+ str(no_of_tweets) + " tweets, reaction of people on '" + topic + "' is: " + avg_reaction)

# function to calculate percentage
def percentage (x, total):
    percent = 100 * float(x)/float(total)
    return format(percent, '.2f')

# calculating percentage of +ve, -ve or neutral reactions
positive_percent = percentage(positive, no_of_tweets)
neutral_percent = percentage(neutral, no_of_tweets)
negative_percent = percentage(negative, no_of_tweets)


def plotPieChart(positive_percent, neutral_percent, negative_percent, topic, no_of_tweets):
    labels = ['Positive [' + str(positive_percent) + '%]',  'Neutral [' + str(neutral_percent) + '%]', 'Negative [' + str(negative_percent) + '%]']
    sizes = [positive_percent, neutral_percent, negative_percent]
    colors = ['blue','green', 'red']
    patches, texts = plt.pie(sizes, colors=colors, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.title("Based on analysis of "+ str(no_of_tweets) + " tweets, average reaction of people on '" + topic + "' is")
    plt.axis('equal')
    plt.tight_layout()
plt.show()

plotPieChart(positive_percent, neutral_percent, negative_percent, topic, no_of_tweets)
