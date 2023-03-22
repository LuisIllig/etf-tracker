from pymongo.database import Database

from overview.overview_scrapper import OverviewScrapper
from overview.ishares import IShares
from overview.amundi import Amundi
from overview.justetf import JustETF
from etf import Etf


class OverviewScrapperStrategy:
    def __init__(self, scrapper: OverviewScrapper):
        self.scrapper = scrapper

    def get_overview(self, dryrun: bool = False):
        return self.scrapper.get_overview(dryrun)


def strategy_selector(etf: Etf, db: Database):
    strategy = None
    match etf.product_family:
        case 'Amundi':
            strategy = JustETF(etf, db)
        case 'iShares':
            strategy = IShares(etf, db)
    return OverviewScrapperStrategy(strategy)
