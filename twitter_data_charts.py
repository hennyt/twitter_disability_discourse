import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import collections
import csv
import tweepy as tw
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob
import re
import networkx

import warnings
warnings.filterwarnings("ignore")

sns.set(font_scale=1.5)
sns.set_style("whitegrid")

set_tweets_list = []

with open("cleaned_tweets.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for i in reader:
        i = i[3]
        for l in i.split():
            set_tweets_list.append(l.lower())

stop_words = set(stopwords.words('english'))

tweets_nsw_nc = []

for word in set_tweets_list:
    if word not in stop_words and word != 'amp' and word not in ['dont', 'cant','im','ive','pulte','anthonyyang'] and word not in ['disability','everydaydisablism','fibromyalgia','chronicpain']:
        tweets_nsw_nc.append(word)

#tweets_nsw = [[word for word in tweet_words if not word in stop_words]for tweet_words in set_tweets_list]
def fig_1_chart():
    counts_no_urls = collections.Counter(tweets_nsw_nc)
    clean_tweets_nsw_nc = pd.DataFrame(counts_no_urls.most_common(30),
                             columns=['words', 'count'])
    fig, ax = plt.subplots(figsize=(8, 8))

# Plot horizontal bar graph
    clean_tweets_nsw_nc.sort_values(by='count').plot.barh(x='words',y='count',ax=ax,color="purple")
    ax.set_title("Common Words Found in Tweets (Excluding Stopwords and Collection Words)")
    plt.show()


def fig_2_chart():
    textblob_list = []
    sentiment_list = []
    with open("cleaned_tweets.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for i in reader:
            textblob_list.append(TextBlob(i[3]))

    for i in textblob_list:
        sentiment_list.append(i.polarity)

    df = pd.read_csv("cleaned_tweets.csv")
    df = pd.DataFrame(data = df, columns = ['cleaned_tweets'])
    new_column = pd.DataFrame({'polarity': sentiment_list})
    df = df.merge(new_column, left_index = True, right_index = True)
    df2 = pd.DataFrame(data = df, columns = ['polarity','cleaned_tweets'])
    df2.to_csv(r'polarity_tweets.csv', index = None, header = True)
    df2 = df[df2.polarity != 0]
    fig, ax = plt.subplots(figsize=(8, 6)) # Plot histogram of the polarity values
    df2.hist(bins=[-1, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1],
             ax=ax,
             color="purple")# Plot histogram with break at zero

    plt.title("Sentiments from Tagged Tweets Related to Disability")
    plt.show()

fig_1_chart()

fig_2_chart()
