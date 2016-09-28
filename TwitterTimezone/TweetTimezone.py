# Import the required libraries.
import tweepy
import pandas as pd
import matplotlib.pyplot as plt

consumerKey = 'YOUR CONSUMER KEY'
consumerSecret = 'YOUR SECRET KEY'

# Use tweepy.OAuthHandler to create an authentication using the given key and secret
auth = tweepy.OAuthHandler(consumer_key=consumerKey, 
    consumer_secret=consumerSecret)

# Connect to the Twitter API using the authentication
api = tweepy.API(auth)

hashtag = raw_input('Enter hashtag to analyze > ')

# Perform a basic search query where we search for the'hashtag' in the tweets
result = api.search(q='%23' + hashtag) #%23 is used to specify '#'

tweet = result[0] #Get the first tweet in the result

results = []

# Get the first 5000 items based on the search query
for tweet in tweepy.Cursor(api.search, q='%23' + hashtag).items(5000):
    results.append(tweet)

# Create a function to convert a given list of tweets into a Pandas DataFrame.

def toDataFrame(tweets):

    DataSet = pd.DataFrame()

    DataSet['tweetID'] = [tweet.id for tweet in tweets]
    DataSet['tweetText'] = [tweet.text for tweet in tweets]
    DataSet['tweetRetweetCt'] = [tweet.retweet_count for tweet 
    in tweets]
    DataSet['tweetFavoriteCt'] = [tweet.favorite_count for tweet 
    in tweets]
    DataSet['tweetSource'] = [tweet.source for tweet in tweets]
    DataSet['tweetCreated'] = [tweet.created_at for tweet in tweets]


    DataSet['userID'] = [tweet.user.id for tweet in tweets]
    DataSet['userScreen'] = [tweet.user.screen_name for tweet 
    in tweets]
    DataSet['userName'] = [tweet.user.name for tweet in tweets]
    DataSet['userCreateDt'] = [tweet.user.created_at for tweet 
    in tweets]
    DataSet['userDesc'] = [tweet.user.description for tweet in tweets]
    DataSet['userFollowerCt'] = [tweet.user.followers_count for tweet 
    in tweets]
    DataSet['userFriendsCt'] = [tweet.user.friends_count for tweet 
    in tweets]
    DataSet['userLocation'] = [tweet.user.location for tweet in tweets]
    DataSet['userTimezone'] = [tweet.user.time_zone for tweet 
    in tweets]

    return DataSet

# Pass the tweets list to the above function to create a DataFrame
DataSet = toDataFrame(results)

# 'None' is treated as null here, so I'll remove all the records having 'None' in their 'userTimezone' column
DataSet = DataSet[DataSet.userTimezone.notnull()]

# Count the number of tweets in each time zone and get the first 10
tzs = DataSet['userTimezone'].value_counts()[:10]
print tzs

# Create a bar-graph figure of the specified size
plt.rcParams['figure.figsize'] = (15, 5)

# Plot the Time Zone data as a bar-graph
tzs.plot(kind='bar')

# Assign labels and title to the graph to make it more presentable
plt.xlabel('Timezones')
plt.ylabel('Tweet Count')
plt.title('Top 10 Timezones tweeting about #' + hashtag)

# the (block = True) is kind of hackey...probably a better way
plt.tight_layout()
plt.show(block = True)