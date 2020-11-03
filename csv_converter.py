import pandas as pd
import numpy as np
import time


headers = [
    'timestamp', 'title', 'category', 'href', 'date_ymd',
    'date_hms', 'date_full', 'is_breaking_news', 'article_text'
]


list_of_paths_to_process = [
    'data/oct_2019_1102_1001.pickle',
    'data/nov_2019_1202_1101.pickle',
    'data/dec_2020_0102_1201.pickle',
    'data/jan_2020_0202_0101.pickle',
    'data/feb_2020_0302_0201.pickle',
    'data/mar_2020_0401_0301.pickle',
    'data/apr_2020_0421_0330.pickle',
]


def basic_processing(df):
    # cleaning
    df = df[df.article_text.notnull()]
    df = df.loc[~df.timestamp.duplicated(keep='first')]

    # transforming
    arr = df.groupby('date_ymd')['timestamp'].nunique()
    df_ = pd.DataFrame(
        {'date_ymd': arr.index, 'number_of_articles_per_day': arr.values})
    key_list = list(df['date_ymd'])
    dict_lookup = dict(zip(df_['date_ymd'], df_['number_of_articles_per_day']))
    df['number_of_articles_per_day'] = [dict_lookup[item] for item in key_list]
    df['article_text'] = df['article_text'].str.replace('\t', '')
    search_for = ['COVID', 'коронавирус',]
    df['covid_related'] = df['article_text'].\
        apply(lambda x: True if any(i in x for i in search_for) else False)
    # print(df['covid_related'].value_counts())
    return df


def convert_pickle_files_to_one_csv(list_of_paths_to_process):
    print('\nconverting...')
    path_csv = 'data_of_seven_months_without_article_texts.csv'
    df_0 = pd.DataFrame(columns=headers)
    for _, each_path in enumerate(list_of_paths_to_process):
        unpickled_list = pd.read_pickle(each_path)
        df_1, df_2 = df_0, pd.DataFrame.from_dict(unpickled_list)
        df_0 = df_1.append(df_2, ignore_index=True)

    df = basic_processing(df_0)

    # save all columns except the deleted ones
    del df['article_text']  # it drastically saves space
    df.to_csv(path_csv, sep='|', encoding='utf-8-sig', index=False)

    # display df from csv
    updated_headers = [x for x in headers if x != 'article_text']
    updated_headers += ['number_of_articles_per_day', 'covid_related']
    df = pd.read_csv(path_csv, sep='|', encoding='utf-8-sig',
                     usecols=updated_headers)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df.tail(20))


def main():

    start_time = time.time()
    convert_pickle_files_to_one_csv(list_of_paths_to_process)
    print('\nDONE.\n')
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":

    main()