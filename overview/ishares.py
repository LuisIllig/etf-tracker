from overview.overview_scrapper import OverviewScrapper
from etf import Etf


url = ''


class IShares(OverviewScrapper):
    def __init__(self, etf: Etf):
        super().__init__(etf)

    def get_overview(self):
        print(self.etf.isin)
