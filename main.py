from extracting import Extractor
from cleaning import Cleaner
import time
# import os
# import csv


# all info with articles from the 2019.10.01 up to 2020.04.21
list_of_paths_to_process = [
    'data/oct_2019_1102_1001.pickle',
    'data/nov_2019_1202_1101.pickle',
    'data/dec_2020_0102_1201.pickle',
    'data/jan_2020_0202_0101.pickle',
    'data/feb_2020_0302_0201.pickle',
    'data/mar_2020_0401_0301.pickle',
    'data/apr_2020_0421_0330.pickle',
]

# The date format '2019_1102_1001' means:
# 2019 is a year, 1102 is 11th month and 2 day, 1001 is 10th month and 1 day
# So 1102 is the top date, 1001 is the bottom date,
# the info was saved from the top date to the bottom date.
# So everything from 10.01 up to 11.02 was saved as 1-month file ~ 30 days


def extracting():
    print('\n\n\nextracting...')
    path_to_extract = 'data/test_0.pickle'  # be aware of 'unix/path'
    extractor = Extractor(path_to_extract)
    extractor.run()


def cleaning():
    print('\n\n\ncleaning...')
    instance_of_workspace = Cleaner(list_of_paths_to_process)
    instance_of_workspace.show_basic_info()
    instance_of_workspace.save_df_as_image('output_images/data_as_is')
    instance_of_workspace.drop_redundant_data()
    instance_of_workspace.save_df_as_image('output_images/cleared_data')


def analyzing():
    # estimated time is about ~ 2 mins
    print('\n\n\nanalyzing...')
    instance_of_workspace = Cleaner(list_of_paths_to_process)
    instance_of_workspace.drop_redundant_data()
    instance_of_workspace.show_basic_info()
    df = instance_of_workspace.df
    print(df.shape)
    print(df)
    text = ' '.join(df['article_text'].tolist())
    # print(text[:300])
    text = text.lower()
    import string
    # print(string.punctuation)
    spec_chars = string.punctuation + '\n\xa0«»\t—…' 
    # print(spec_chars)

    print('\n\n\nanalyzing...')
    
    text = "".join([ch for ch in text if ch not in spec_chars])
    text = "".join([ch for ch in text if ch not in string.digits])

    from nltk import word_tokenize
    text_tokens = word_tokenize(text)

    from nltk.corpus import stopwords
    russian_stopwords = stopwords.words("russian")
    russian_stopwords.extend(
        [
            'это', 
            'также',
            'которые',
            'который',
            'которых',
            'которая',
            'тасс',
            'года',
            'году',
            'лет',
            'ранее',
            'изза',
            'числе',
            'очень',
            'пока',
        ]
    )

    # print(len(russian_stopwords))
    text_tokens = [token.strip() for token in text_tokens if token not in russian_stopwords]
    print('len(text_tokens): ' + str(len(text_tokens)))

    import nltk
    text = nltk.Text(text_tokens)

    fdist_sw = nltk.FreqDist(text)
    print('list of the most common words: (Oct 2019 -> Apr 2020)')
    print(fdist_sw.most_common(100))


def main():

    start_time = time.time()

    # extracting()  # saves the data to .pickle

    # cleaning()  # reads list of .pickle files and cleans that

    analyzing()  # uses all previous steps to make a final conclusion, prints info about the text

    print('\nDONE.\n')
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":

    main()
