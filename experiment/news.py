import feedparser
from datetime import datetime, timedelta
from dateutil import parser


def is_within_24_hours(published_date):
    # Parse the published date string into a datetime object
    pub_date = parser.parse(published_date)

    # Calculate the time difference between now and the published date
    time_difference = datetime.now(pub_date.tzinfo) - pub_date

    # Check if the time difference is less than 24 hours
    return time_difference < timedelta(hours=24)

def ign():
    #d = feedparser.parse('http://feeds.feedburner.com/ign/games-all')
    #d = feedparser.parse('http://feeds.feedburner.com/ign/comics-articles')
    #d = feedparser.parse('http://feeds.feedburner.com/ign/game-reviews')
    #d = feedparser.parse('http://feeds.feedburner.com/ign/all')


    for header in d['entries']:
        if is_within_24_hours(header['published']):
            #print(header)
            print(header['title'], header['description'], header['published'])






def google():
    #d = feedparser.parse('https://news.google.com/rss/search?q=zurich&hl=ch-DE')
    #d = feedparser.parse('https://news.google.com/rss/search?q=Playstation&hl=ch-DE&gl=CH&ceid=CH:de&scoring=n&as_occt=1&as_drrb=b&as_mindate=now-1d&num=10')
    d = feedparser.parse('https://news.google.com/rss/search?q=site:tagesanzeiger.ch+OR+site:nzz.ch&hl=de&gl=DE&ceid=DE:de&scoring=n&as_occt=1&as_drrb=b&as_mindate=now-1d')


    for header in d['entries']:
        if is_within_24_hours(header['published']):
            #print(header)
            print(header['title'], header['published'])

ign()
google()
