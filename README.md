# Code Examples

Seven projects are contained in this repository.  The projects, and how to run them locally (when applicable), are described below.

## TwitterTimezone 

This application captures data from the Twitter API via Tweepy, stores it in a Pandas dataframe, and visualizes it through matplotlib. This example graphs the top 10 timezones tweeting about a hashtag (first 5000 items).

To install, download the file, and add your keys in these positions
```
consumerKey = 'YOUR CONSUMER KEY'
consumerSecret = 'YOUR SECRET KEY'
```
run
```
pip install tweepy
pip install pandas
pip install matplotlib
```
then call
```
python TweetTimezone.py
```
when prompted, enter the topic/hashtag you want to analyze (no # needed).

## SpeedTweet

The application combines experimentation with Tweepy and the Twitter API with the "Speed Reader" tool below. It captures tweets abgout a keyword(s) in near real-time, and displays them in a fashion similar to [spritz](http://spritzinc.com/). To install, download the file, and add your keys in these positions
```
ckey = 'YOUR CONSUMER KEY'
csecret = 'YOUR SECRET KEY'
atoken = 'YOUR ACCESS TOKEN'
asecret = 'YOUR SECRET TOKEN'
```
then run
```
python SpeedTweet.py
```
You will be prompted to enter a "desired reading rate" in words-per-minute (something around 150-200 is a good place to start).

You will then be prompted to enter keywords to track, seperated by spaces. Popular topics work well because there won't be a break in the stream of information.


## Politicheck

Scraped and pickled the [Poilitifact](http://www.politifact.com/) website. The application loads the corpus, preprocesses, then prompts for text to analyze. To install, download the files, run
```
python cl.py
```
You will be prompted to enter a topic to analyze. Try something like "guns", "environment", "health".

## Will You Like Me

[Will You Like Me](http://williamsplace.synology.me/harriette/wylm/index.html) was a group project developed for a capstone Data Visualization class. The linked instance is using a static sample data (it would generally require you to login to Facebook to extract personal posting history, friends, etc.) To see how the tool works try typing
```
Does anyone want to go to boston today? We can go down to the harbor and follow the parade.
```
The application updates as new keywords are detected and visualizes how predicted likes, likers, and recommend words change as you try out posts.

For a sample of the code I developed, look at *getFriends.py*

## News Website Summarizer

This was a quick and simple command line news scraper and summarizer, built using the [newspaper.py](https://pypi.python.org/pypi/newspaper) library while evaluating the library for other projects.  To install, download the file, run
```
pip install newspaper
```
then call
```
python NewsSummary.py
```
## Surveillance Map

This [surveillance map](https://activism.tech/map.html) was developed a part of [activism.tech](https://activism.tech), as a tool to visualize global surveillance as well as give people to ability to plan routes with camera locations in mind.

Only a small number of cameras are included for ease of dowload and testing.

There are quite a few packages required to render and run the map, including Leaflet.js, OSM Geocoder, OSM GeoSearch, MarkerCluster, etc. so spinning up a working system locally may take a little time.

## Speed Reader

This tool was inspired by my previous experiments with [newspaper.py](https://pypi.python.org/pypi/newspaper), as well as speed-reading services such as [spritz](http://spritzinc.com/).  The intent is to allow command-line speed reading of news articles.

To run locally, clone the directory, then run
```
pip install newspaper
```
then run
```
python ithkuil.py
```
and follow the instructions.
```.
