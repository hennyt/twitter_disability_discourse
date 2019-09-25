import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import collections
import csv
import tweepy as tw
import nltk
from nltk.corpus import stopwords
import re
import networkx

import warnings
warnings.filterwarnings("ignore")

sns.set(font_scale=1.5)
sns.set_style("whitegrid")

clean_tweets = []
def remove_url():
    with open("tweepy_api_raw_tweets.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for i in reader:
            clean_tweets.append(" ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", i[2]).split()))

    """Replace URLs found in a text string with nothing
    (i.e. it will remove the URL from the string).

    Parameters
    ----------
    txt : string
    A text string that you want to parse and remove urls.

    Returns
    -------
    The same txt string with url's removed.
    """

    #return "executed"

remove_url()
df = pd.read_csv('tweepy_api_raw_tweets.csv')
new_column = pd.DataFrame({'cleaned_tweets': clean_tweets})
df = df.merge(new_column, left_index = True, right_index = True)
df2 = pd.DataFrame(data = df, columns = ['user', 'location', 'cleaned_tweets'])
df2.to_csv('cleaned_tweets.csv')
