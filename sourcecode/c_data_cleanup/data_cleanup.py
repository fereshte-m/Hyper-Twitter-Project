import pandas as pd
import csv
import re

import nltk.corpus
nltk.download('stopwords')
from nltk.corpus import stopwords

hashtag_list = ["HoseinRonaghi", "IranRevolution", "MahsaAmini", "MohsenShekari", "OpIran", "WomenLifeFreedom"]


def cleanup_mentions(hashtag: str):
    """
    This function cleans mentions, stop words, unicode characters
    :return:
    """

    print(f"cleaning up ./{hashtag}_cleanup.csv")
    # creating/writing a csv file - calling the text as a column
    csv_file = open(f'./{hashtag}_cleanup.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Text"])

    # reading the original csv file and printing as a column
    df = pd.read_csv(fr'../b_data_filter/{hashtag}_filter.csv')

    #  1. normalizing (the loop) text by making it lowercase
    for index, row in df.iterrows():
        text = row['Text'].lower()

        # 2. normalizing (loop body) the text by removing unicode characters
        text = re.sub(r"([^0-9A-Za-z#@ \t])|(\w+:\/\/\S+)|^rt|http.+?", " ", text)

        # 3.1 normalizing (loop body) the text by removing stopwords
        stop = stopwords.words('english')
        text = " ".join([word for word in text.split() if word not in stop])

        # 3.2 remove the below list fo words from the text
        to_be_removed_list = ["the", "this", "that", "by", "in", "on", "or", "of", "thats"]
        text_as_list = text.split()
        for word in to_be_removed_list:
            if word in text_as_list:
                text_as_list.remove(word)

        # 3.3 rejoining the words from list to text
        text = " ".join([word for word in text_as_list])
        csv_writer.writerow([text])


for hashtag in hashtag_list:
    cleanup_mentions(hashtag)
