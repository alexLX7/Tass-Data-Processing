from extractor import Extractor
import time


def main():

    start_time = time.time()
    path = 'data/test_0.pickle'  # be aware of 'unix/path'

    print('extracting...')
    extractor = Extractor(path)
    extractor.run()

    print('\nDONE.')
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":

    main()
