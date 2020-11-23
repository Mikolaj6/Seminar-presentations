import re
import argparse
import pickle

from bs4 import BeautifulSoup
import requests
from requests import HTTPError
from stop_words import get_stop_words


parser = argparse.ArgumentParser()
parser.add_argument("websites_to_scrape_path", help="Path to file with listed websites to scrape.")
parser.add_argument("res_file", help="Path to file where scraping results will be stored.")
args = parser.parse_args()


def get_custom_headers():
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Save-Data": "on",
        "Accept-Encoding": ", ".join(("gzip", "deflate")),
        "Accept": "*/*",
        "Connection": "keep-alive"
    }
    return headers


def scrape_all():
    X = []
    Y = []

    with open(args.websites_to_scrape_path, 'r') as f_read:
        for line in f_read.readlines():
            line_data = line.strip().split(' ')
            if len(line_data) != 2:
                print('Bad line: {0}'.format(line))
                continue

            try:
                response = requests.get(line_data[1], headers=get_custom_headers())
                response.raise_for_status()
            except HTTPError as http_err:
                print('HTTP error has occurred: {0} at {1}'.format(http_err, line_data[1]))
            except Exception as err:
                print('Other error has occurred: {0} at {1}'.format(err, line_data[1]))
            else:
                soup = BeautifulSoup(response.text, 'html.parser')
                text = soup.get_text()

                X.append(text)
                Y.append(line_data[0] == "TRUE")

            print('Scraped {0}'.format(line_data[1]))

    x_preprocessed_ = preprocess_text(X)
    x = preprocess_basic(X)
    return x_preprocessed_, x, Y


def preprocess_basic(X):
    x_new = []

    for text in X:
        text = text.strip()
        text = re.sub(r'[0-9]', ' ', text)
        x_new.append(' '.join(text.split()))

    return x_new


def preprocess_text(X):
    x_new = []

    for text in X:
        text = text.strip()
        text = re.sub(r'[^a-zA-ZĄąĆćĘęŁłŃńÓóŚśŹźŻż\s]', ' ', text)

        tokens = text.split()

        # Remove stop words
        stop_words = set(get_stop_words('polish'))
        tokens = [i for i in tokens if i not in stop_words]
        x_new.append(' '.join(tokens))

    return x_new


x_preprocessed, x_original, y = scrape_all()


res = {
    'x_preprocessed': x_preprocessed,
    'x_original': x_original,
    'y': y
}

with open(args.res_file, 'wb') as f_write:
    pickle.dump(res, f_write)
