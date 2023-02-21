from pymongo.database import Database

from overview.overview import *
from overview.overview_scrapper import OverviewScrapper
from etf import Etf
from bs4 import BeautifulSoup

from utility import get_soup


base_url = 'https://www.ishares.com'
passthrough_parameters = '?switchLocale=y&siteEntryPassthrough=true'
list_parameters = '&showAll=true#/?productView=all&pageNumber=1&sortColumn=totalFundSizeInMillions&sortDirection=desc&dataView=keyFacts&keyFacts=all&showAll=true'
product_list_url = f'/de/privatanleger/de/produkte/etf-investments{passthrough_parameters}{list_parameters}'

class IShares(OverviewScrapper):
    def __init__(self, etf: Etf, db: Database):
        super().__init__(etf, db)

    def get_overview(self):
        print(self.etf.isin)
        product_url = self.search_etf()
        if product_url is not None:
            soup = get_soup(base_url + product_url + passthrough_parameters)
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

    # noinspection PyMethodMayBeStatic
    def get_performance(self, soup: BeautifulSoup) -> list[Performance]:
        table = soup.find('table', {'class': 'product-table border-row calendar-year'})

        thead = table.find('thead')
        ths = thead.find_all('th')
        performance = []
        for th in range(1, len(ths)):
            performance.append(Performance(ths[th].text, None, None))

        tbody = soup.find('tbody')
        trs = tbody.find_all('tr')
        tr_total_return = trs[0]
        tr_benchmark = trs[1]

        tds = tr_total_return.find_all('td')
        for td in range(1, len(tds)):
            performance[td - 1].total_return = tds[td].text.replace('\n', '')
        tds = tr_benchmark.find_all('td')
        for td in range(1, len(tds)):
            performance[td - 1].benchmark = tds[td].text.replace('\n', '')

        return performance

    def get_portfolio(self, soup: BeautifulSoup) -> Portfolio:
        pass

    def update_overview(self, overview: Overview):
        pass
