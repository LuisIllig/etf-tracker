from abc import ABC, abstractmethod

from pymongo.database import Database

from etf import Etf


class OverviewScrapper(ABC):
    def __init__(self, etf: Etf, db: Database):
        self.etf = etf
        self.db = db

    @abstractmethod
    def get_overview(self):
        pass
