import pandas as pd
import numpy as np
import datetime
import requests
import pickle
import time
import re
from bs4 import BeautifulSoup
from pretty_time import *


class Extractor:
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.pretty_time = PrettyTime(
            '2020-04-21 00:00:00',  # Y, m, d, h, m, s
            '2020-04-20 21:00:00'
            # '2020-04-21 00:00:00',  # Y, m, d, h, m, s
            # '2020-03-30 00:00:00'
        )
        # first date is closer to today, the count goes like this:
        # recent news (which are on top) go down below (to the bottom)
        # top time
        self.timestamp_top = self.pretty_time.list_of_dt[0].timestamp()
        # bottom time
        self.timestamp_bottom = self.pretty_time.list_of_dt[1].timestamp()

    def run(self):
        self.write()

    def print_input_dates(self):
        print()
        print('The latest piece of news is up to this date:')
        print(self.pretty_time.list_of_dt[0])
        print(self.timestamp_top)
        print('The oldest piece of news is up to this date:')
        print(self.pretty_time.list_of_dt[1])
        print(self.timestamp_bottom)
        print()

    def print_bottom_dates_borders(self, input_bottom_timestamp, actual_bottom_timestamp):
        print()
        print('The oldest piece of news is up to this date:')
        print(datetime.fromtimestamp(
            int(input_bottom_timestamp)).strftime('%Y-%m-%d %H:%M:%S'))
        print(input_bottom_timestamp)
        print('The last piece of news before the input time contains this date:')
        print(datetime.fromtimestamp(
            int(actual_bottom_timestamp)).strftime('%Y-%m-%d %H:%M:%S'))
        print(actual_bottom_timestamp)
        print()

    def write(self):
        data = []
        current_time = int(self.timestamp_top)
        try:
            while current_time > int(self.timestamp_bottom):
                current_news = self.tass_lenta(current_time)
                if current_news:
                    current_time = current_news[-1]['timestamp']
                    data.extend(current_news)
                    l = len(data)
                    if l % 100 == 0:
                        print('Number of items: ' + str(l))
                else:
                    print('...extracting is finished.')
                    self.print_input_dates()
                    self.print_bottom_dates_borders(
                        self.timestamp_bottom, current_time)
                    print('writing to file...')
                    break
        except Exception as e:
            print('Got exception:')
            print(e.message, e.args)
            print('\nAnyways, writing saved data to file...')
        with open(self.path, 'wb') as f:
            pickle.dump(data, f)
        print('...writing is finished.')

    def html_stripper(self, text):
        return re.sub('<[^<]+?>', '', str(text))

    def validate_parsed_result(self, new_dict, bottom_time):
        if int(new_dict['timestamp']) > int(self.timestamp_bottom):
            return True
        return False

    def tass_lenta(self, before, limit=200):
        # the limit is 200 because it is the max amount of items on the page
        # before it asks to reload for the next 200 items
        mainpage = 'http://tass.ru/api/news/lenta?limit=' + \
            str(limit)+'&before='+str(before)
        # print(mainpage)
        response = requests.get(mainpage)
        dict_of_response = response.json()
        cur_news = []
        df = dict_of_response['articles']
        tass_link = 'https://tass.ru'
        for item in df:
            try:
                new = {}

                item_url = str(item['url'])
                new['timestamp'] = int(item['time'])
                # have to save other vars too

                new['title'] = item['title']
                new['category'] = item['section']['title']
                new['href'] = item_url
                new['date_ymd'] = datetime.fromtimestamp(
                    int(item['time'])).strftime('%Y-%m-%d')
                new['date_hms'] = datetime.fromtimestamp(
                    int(item['time'])).strftime('%H:%M:%S')
                new['date_full'] = datetime.fromtimestamp(
                    int(item['time'])).strftime('%Y-%m-%d %H:%M:%S')
                new['is_breaking_news'] = item['is_breaking_news']
                new['article_text'] = None

                # try:
                #     soup = BeautifulSoup(
                #         requests.get(
                #             # str(tass_link) + str(item['url'])
                #             f'{tass_link}{item_url}'
                #         ).text,
                #         'html.parser'
                #     )
                #     article_text = ''
                #     article = soup.find(
                #         "div", {"class": "text-block"}).findAll('p')
                #     for element in article:
                #         article_text += '\n' + \
                #             ''.join(element.findAll(text=True))
                #     new['article_text'] = str(article_text)
                # except:
                #     pass

                if self.validate_parsed_result(new, before):
                    cur_news.append(new)
            except:
                print('Error: \n', item_url, '\n')
        return cur_news
