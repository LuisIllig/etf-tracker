from dotenv import dotenv_values
from pymongo import MongoClient

from masterdata import Masterdata

config = dotenv_values('.env')

mongo_client = MongoClient(config['mongo_uri'])
db = mongo_client.etfTrackerDB


def main():
    masterdata = Masterdata(config, db)
    masterdata.update(skip_download=True)


if __name__ == '__main__':
    main()
