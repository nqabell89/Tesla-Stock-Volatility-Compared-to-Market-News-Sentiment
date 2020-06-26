from twitterscraper import query_tweets


def tweets(ticker, name, start=2006-01-01, end=2020-01-01):
	list_of_tweets = query_tweets(f'(${ticker} OR {name}) (from:wsj OR from:reuters OR from:business OR from:cnbc OR from:RANsquawk OR from:wsjmarkets) until:{end} since:{start}', 10000)
	return list_of_tweets

import seaborn as sns
import pandas as pd
