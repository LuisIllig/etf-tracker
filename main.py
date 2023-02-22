from dotenv import dotenv_values
from pymongo import MongoClient
from masterdata import Masterdata
from overview.overview_scrapper_strategy import strategy_selector

config = dotenv_values('.env')

mongo_client = MongoClient(config['mongo_uri'])
db = mongo_client.etfTrackerDB


def main():
    masterdata = Masterdata(config, db, dryrun=True)
    etfs = masterdata.update()
    print(config['tracked_etfs'])
    for etf in etfs:
        if etf.isin in config['tracked_etfs']:
            strategy_selector(etf, db).get_overview(dryrun=True)


if __name__ == '__main__':
    main()
