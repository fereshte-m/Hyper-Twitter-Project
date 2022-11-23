import pandas as pd
import csv

hashtag_list = ["HoseinRonaghi", "IranRevolution", "MahsaAmini", "MohsenShekari", "OpIran", "WomenLifeFreedom"]


def filter_data(hashtag: str):
    # creating/writing a csv file - calling the text as a column
    csv_file = open(f'{hashtag}_filter.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Text"])

    # reading the original csv file and printing as a column
    df = pd.read_csv(fr'../a_data_fetch/{hashtag}_fetch.csv')

    # writing a loop for filtering the language to English, as well as extracting the Text of each Tweet
    for index, row in df.iterrows():
        if 'language' in row and (row['language'] == "en" or row['language'] == "und"):
            csv_writer.writerow([row['Text']])


for hashtag in hashtag_list:
    filter_data(hashtag)
