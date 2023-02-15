from overview.overview_scrapper import OverviewScrapper
from overview.ishares import IShares
from overview.amundi import Amundi
from etf import Etf


class OverviewScrapperStrategy:
    def __init__(self, scrapper: OverviewScrapper):
        self.scrapper = scrapper

    def get_overview(self):
        return self.scrapper.get_overview()


def strategy_selector(etf: Etf):
    strategy = None
    match etf.product_family:
        case 'Amundi':
            strategy = Amundi(etf)
        case 'iShares':
            strategy = IShares(etf)
    return OverviewScrapperStrategy(strategy)
