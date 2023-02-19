from pymongo.database import Database

from overview.overview import *
from overview.overview_scrapper import OverviewScrapper
from etf import Etf
from bs4 import BeautifulSoup

from utility import get_soup


base_url = 'https://www.ishares.com'
product_list_url = '/de/privatanleger/de/produkte/etf-investments?switchLocale=y&siteEntryPassthrough=true&showAll=true#/?productView=all&pageNumber=1&sortColumn=totalFundSizeInMillions&sortDirection=desc&dataView=keyFacts&keyFacts=all&showAll=true'


class IShares(OverviewScrapper):
    def __init__(self, etf: Etf, db: Database):
        super().__init__(etf, db)

    def get_overview(self):
        print(self.etf.isin)
        product_url = self.search_etf()
        if product_url is not None:
            soup = get_soup(base_url + product_url)
            performance = self.get_performance(soup)
            portfolio = self.get_portfolio(soup)
            overview = Overview(self.etf.id, performance, portfolio)
        else:
            print(f'No product found for {self.etf.isin}: {self.etf.name}')

    def search_etf(self) -> str | None:
        soup = get_soup(base_url + product_list_url)
        a = soup.find('a', string=self.etf.xetra_symbol)
        if a is not None:
            return a['href']
        return None

    def get_performance(self, soup: BeautifulSoup) -> list[Performance]:
        pass

    def get_portfolio(self, soup: BeautifulSoup) -> Portfolio:
        pass

    def update_overview(self, overview: Overview):
        pass
