from extracting import Extractor
from cleaning import Cleaner
import time


# all info from the 2019.10.01 up to 2020.04.21
list_of_paths_to_process = [
    'data/oct_2019_1102_1001.pickle',
    'data/nov_2019_1202_1101.pickle',
    'data/dec_2020_0102_1201.pickle',
    'data/jan_2020_0202_0101.pickle',
    'data/feb_2020_0302_0201.pickle',
    'data/mar_2020_0401_0301.pickle',
    'data/apr_2020_0421_0330.pickle',
]

# '2019_1102_1001' means: 2019 - year, 1102 is 11th month and the 2nd day, 1001 is 10th month and the 1st day
# The info was saved from the top date to the bottom date:
# 1102 is the top date, 1001 is the bottom date,
# So everything from 10.01 up to 11.02 was saved as 1-month file


def extracting():
    print('\n\n\nextracting...')
    path_to_extract = 'data/test_0.pickle'
    extractor = Extractor(path_to_extract)
    extractor.run()


def cleaning():
    print('\n\n\ncleaning...')
    instance_of_workspace = Cleaner(list_of_paths_to_process)
    instance_of_workspace.show_basic_info()
    instance_of_workspace.save_df_as_image('output_images/data_as_is.png')
    instance_of_workspace.drop_redundant_data()
    instance_of_workspace.save_df_as_image('output_images/cleared_data.png')


def main():

    start_time = time.time()

    # extracting()  # saves the data to .pickle

    # cleaning()  # reads list of .pickle files and cleans that list

    # analyzing()  # check 'analyzing.ipynb', there are a few pieces of info about the text

    print('\nDONE.\n')
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":

    main()
