# Code Samples

Four projects are contained in this repository.  The projects, and how to run them locally (when applicable), are described below.

## Will You Like Me

[Will You Like Me](http://williamsplace.synology.me/harriette/wylm/index.html) was a group project developed for a capstone Data Visualization class. The linked instance is using a static sample data (it would generally require you to login to Facebook to extract personal posting history, friends, etc.) To see how the tool works try typing
```
Does anyone want to go to boston today? We can go down to the harbor and follow the parade.
```
The application updates as new keywords are detected and visualizes how predicted likes, likers, and recommend words change as you try our posts.

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
