import numpy as np
import time
import pandas as pd
import pickle


class Cleaning:
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.df = None
        self.init()
        print(self.df.head())

    def init(self):
        with open(self.path, 'rb') as f:
            data = pickle.load(f)
        self.df = pd.DataFrame(data)


class Draft:
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.df = None

    def set_df(self):
        with open(self.path, 'rb') as f:
            data = pickle.load(f)
        return pd.DataFrame(data)

    def print_head(self):
        print(self.df.head())

    def print_shape(self):
        print(self.df.shape)

    def print_all_categories(self):
        s = pd.Series(list(set(self.df['category'])))  # 15 categories in total
        print(s)
        print(s.describe())

    def print_describe_category(self):
        s = pd.Series(self.df['category'])
        print(s.describe())

    def has_virus(self, input_):

        pass
        # print(type(input_))
        # print(input_)

    def process_(self, df):
        df['related_to_virus'] = df['article_text'].str.contains(
            'covid|вирус', regex=True)
        # pass
        # df['related_to_virus'] = self.has_virus(df['title'])
        print(df)

        # for index, value in df.items():
        #     print(f"Index : {index}, Value : {value}")

    def test_0(self):
        pd.set_option('display.max_columns', None)
        df = self.set_df()

        print(df.shape)
        # self.process_(df)
        # print(df)

        # print(df['title'])

        # df = df.groupby('date')['href'].nunique()
        # print (df)

        # print(df.shape)
        # print(df.head())

        # df[df.duplicated(keep=False)]
        # print(df.shape)
        # print(df.head())

        # # ids = df["href"]  # list_of_unique_hrefs
        # # new_df = df[ids.isin(ids[ids.duplicated()])] # .sort("href")
        # # new_df = pd.concat(g for _, g in df.groupby("href") if len(g) > 1)
        # print(new_df.shape)
        # print(new_df.head())

        # df.drop_duplicates(keep=False, inplace=True)
        # print(df.shape)
        # print(df.head())

    def run(self):
        self.test_0()
