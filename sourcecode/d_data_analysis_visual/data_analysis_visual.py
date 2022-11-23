import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import csv
import nltk.corpus
nltk.download('stopwords')
from nltk.corpus import stopwords
from hazm import word_tokenize
import hazm


# Define a counter to count each word,tag and hashtag
def word_counter(word_list):
    d = {}
    for key in word_list:
        d[key] = d.get(key, 0) + 1

    # Next, sort from highest to lowest.
    number_of_key = sorted(d.items(), key=lambda x: x[1], reverse=True)

    return number_of_key


def load_prepare_data(hashtag: str):
    """
    This function load and prepares data based on given hashtag. It sorts
    :param hashtag:
    :return:
    """
    data_cleaned = pd.read_csv(fr'../c_data_cleanup/{hashtag}_cleanup.csv')
    data_cleaned.head()

    # We add all of the rows in a string:
    final_text = data_cleaned['Text'].str.cat(sep='')

    # in the next step we separate each words
    word_list = final_text.split()

    # separate the hashtags and other words
    hashtags = []
    mentions = []
    words = []
    for word in word_list:
        if word[0] == '#':
            hashtags.append(word)
        elif word[0] == '@':
            mentions.append(word)
        else:
            words.append(word)

    word_count = word_counter(words)
    top_25_words = dict(word_count[:25])
    low_25_words = dict(word_count[-25:])

    hashtag_count = word_counter(hashtags)
    top_25_hashtags = dict(hashtag_count[:25])
    low_25_hashtags = dict(hashtag_count[-25:])

    mention_count = word_counter(mentions)
    top_25_mentions = dict(mention_count[:25])
    low_25_mentions = dict(mention_count[-25:])

    return top_25_words, top_25_hashtags, top_25_mentions, low_25_words, low_25_hashtags, low_25_mentions


def plot_section(hashtag, data, x_lable):
    plt.figure(figsize=(14, 6))
    plt.xlabel(x_lable, fontsize=16)
    plt.ylabel('Frequency', fontsize=16)
    plt.title(f'Each {x_lable} Frequency in #{hashtag} on the Twitter', fontsize=18)
    plot = sns.barplot(x=list(data.keys()), y=list(data.values()))
    plot.set_xticklabels(plot.get_xticklabels(), rotation=40, ha="right", fontsize='x-large')


def plot_data(hashtag, word_plot_mode, hashtag_plot_mode, mention_plot_mode):

    sorted_data = load_prepare_data(hashtag)

    data_for_plot = sorted_data[0] if word_plot_mode == 'M' else sorted_data[3]
    plot_section(hashtag, data_for_plot, 'word')

    data_for_plot = sorted_data[1] if hashtag_plot_mode == 'M' else sorted_data[4]
    plot_section(hashtag, data_for_plot, 'hashtag')

    data_for_plot = sorted_data[2] if mention_plot_mode == 'M' else sorted_data[5]
    plot_section(hashtag, data_for_plot, 'mention')

    plt.show()
