from utility import *
from etf import *

import pandas as pd


class Masterdata:
    def __init__(self, config, db, dryrun: bool = False):
        self.config = config
        self.db = db
        self.dryrun = dryrun
        self.etfs = []

    def update(self) -> list[Etf]:
        self.download_masterdata()
        self.etfs = self.parse_masterdata()
        self.update_masterdata(self.etfs)
        return self.etfs

    def download_masterdata(self):
        if self.dryrun:
            print('Skipping download of master data...')
            return

        print('Downloading master data...')
        if not os.path.exists('target'):
            os.makedirs('target')

        all_tradable_etfs = 'target/all_tradable_etfs.xls'

        if not os.path.exists(all_tradable_etfs):
            download_file(self.config['all_tradable_etfs'], all_tradable_etfs)
        else:
            download_file(self.config['all_tradable_etfs'], all_tradable_etfs + '.tmp')
            if os.path.getsize(all_tradable_etfs + '.tmp') > 0:
                replace_if_more_recent(all_tradable_etfs + '.tmp', all_tradable_etfs)

    # noinspection PyMethodMayBeStatic
    def parse_masterdata(self) -> list[Etf]:
        print('Parsing master data...')
        df = pd.read_excel('target/all_tradable_etfs.xls')

        etfs = []
        for row in df.itertuples():
            etfs.append(map_xls(row))

        return etfs

    def update_masterdata(self, etfs: list[Etf]):
        if self.dryrun:
            print('Skipping update of master data...')
            return

        print('Updating master data...')
        coll = self.db.masterdata

        for etf in etfs:
            coll.find_one_and_update({'id': etf.id}, {'$set': etf.__dict__}, upsert=True)

