from abc import ABC, abstractmethod
from etf import Etf


class OverviewScrapper(ABC):
    def __init__(self, etf: Etf):
        self.etf = etf

    @abstractmethod
    def get_overview(self):
        pass
