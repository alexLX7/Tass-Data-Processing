from extracting import Extractor
from cleaning import Cleaner
import time


def extracting():
    print('extracting...')
    path_to_extract = 'data/test_0.pickle'  # be aware of 'unix/path'
    extractor = Extractor(path_to_extract)
    extractor.run()


def cleaning():
    print('cleaning...')

    # all info with articles from the 2019.10.01 up to 2020.04.21
    list_of_paths = [
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
    # I hope it makes sense.

    instance_of_workspace = Cleaner(list_of_paths)
    instance_of_workspace.show_basic_info()
    instance_of_workspace.save_df_as_image()


def main():

    start_time = time.time()

    # extracting()

    cleaning()

    print('\nDONE.\n')
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":

    main()
