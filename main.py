from dotenv import dotenv_values
from etf import map_xls
from pymongo import MongoClient

import sys
import requests
import pandas as pd
import os

config = dotenv_values('.env')


def main():
    print('Hello World')
    all_tradable_etfs = 'target/all_tradable_etfs.xls'

    if not os.path.exists(all_tradable_etfs):
        if not os.path.exists('target'):
            os.makedirs('target')
        download_file(config['all_tradable_etfs'], all_tradable_etfs)

    df = pd.read_excel('target/all_tradable_etfs.xls')

    etfs = []
    for row in df.itertuples():
        etfs.append(map_xls(row))

    mongo_client = MongoClient(config['mongo_uri'])
    db = mongo_client.masterdata
    coll = db.etfs
    # coll.insert_many([etf.__dict__ for etf in etfs])


def download_file(url: str, filename: str, timeout: int = 10):
    try:
        print(f'downloading {filename} from {url}...')
        response = requests.get(url, stream=True, timeout=timeout)
        if response.status_code != 200:
            sys.exit(f'Error: Could not connect to server {url} with status code {response.status_code}')
        with open(filename, 'wb') as f:
            total_length = int(response.headers.get('content-length'))
            dl = 0
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    dl += len(chunk)
                    f.write(chunk)
                    done = int(50 * dl / total_length)
                    bar = '\r[%s%s]' % ('=' * done, ' ' * (50 - done))
                    missing_mb = f' {dl / 1024 / 1024:.2f}MB / {total_length / 1024 / 1024:.2f}MB'
                    sys.stdout.write(bar + missing_mb)
                    sys.stdout.flush()
        print(f'\ndownloaded {filename} from {url}...')
    except requests.exceptions.Timeout:
        sys.exit(f'Error: Timeout while connecting to server {url}')


if __name__ == '__main__':
    main()
