from pymongo.database import Database

from etf import Etf
from overview.overview_scrapper import OverviewScrapper


url = 'www.lyxoretf.de/lyxor-etf-fonds/lyxor-etf-fonds-detailseite.html?isin=FR0011027063'


class Amundi(OverviewScrapper):
    def __init__(self, etf: Etf, db: Database):
        super().__init__(etf, db)

    def get_overview(self):
        print(self.etf.isin)
