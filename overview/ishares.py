import sys

from pymongo.database import Database

from overview.overview import *
from overview.overview_scrapper import OverviewScrapper
from etf import Etf
from bs4 import BeautifulSoup
from jsoncomment import JsonComment
from requests_html import HTMLSession

from utility import get_soup, download_file

from pyppeteer.errors import TimeoutError

import pandas as pd
import re
import json


# https://www.ishares.com/de/privatanleger/de/produkte/251882/ishares-msci-world-ucits-etf-acc-fund


base_url = 'https://www.ishares.com'
passthrough_parameters = '?switchLocale=y&siteEntryPassthrough=true'
list_parameters = '&showAll=true#/?productView=all&pageNumber=1&sortColumn=totalFundSizeInMillions&sortDirection=desc&dataView=keyFacts&keyFacts=all&showAll=true'
product_list_url = f'/de/privatanleger/de/produkte/etf-investments{passthrough_parameters}{list_parameters}'


# noinspection PyMethodMayBeStatic
class IShares(OverviewScrapper):
    def __init__(self, etf: Etf, db: Database):
        super().__init__(etf, db)

    def get_overview(self, dryrun: bool = False):
        print(self.etf.isin)
        product_url = self.search_etf()
        if product_url is not None:
            soup = get_soup(base_url + product_url + passthrough_parameters)
            performance = self.get_performance(soup)
            portfolio = self.get_portfolio(soup, product_url, dryrun)
            return Overview(self.etf.id, performance, portfolio)
        else:
            print(f'No product found for {self.etf.isin}: {self.etf.name}')

    def search_etf(self) -> str | None:
        soup = get_soup(base_url + product_list_url)
        a = soup.find('a', string=self.etf.xetra_symbol)
        if a is not None:
            return a['href']
        return None

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

    def get_portfolio(self, soup: BeautifulSoup, url: str,  dryrun: bool) -> Portfolio:
        positions = self.get_positions(soup, dryrun)
        response = self.get_response_with_js(url)
        sectors = self.get_sectors(response)
        geography = self.get_geography(response)
        return Portfolio(positions, sectors, geography)

    def get_positions(self, soup: BeautifulSoup, dryrun: bool) -> list[Position]:
        href = soup.find('a', {'class': 'icon-xls-export', 'data-link-event': 'holdings:holdings'})['href']
        csv_file = f'target/{self.etf.isin}.csv'
        if not dryrun:
            download_file(base_url + href, csv_file)
        positions = []
        df = pd.read_csv(csv_file, sep=',', skiprows=2, skipfooter=1, engine='python')
        for index, row in df.iterrows():
            positions.append(Position(row[0], row[1], row[2], row[3], row[5]))
        return positions

    def get_sectors(self, response: str) -> list[Sector]:
        data = self.find_by_var(response, 'tabsSectorDataTable')

        sectors = []
        for entry in data:
            category = entry['name']
            fonds = entry['value']
            sectors.append(Sector(category, fonds))
        return sectors

    def get_geography(self, response: str) -> list[Geography]:
        data = self.find_by_var(response, 'subTabsCountriesDataTable')

        geography = []
        for entry in data:
            country = entry['code']
            fonds = entry['value']
            geography.append(Geography(country, fonds))
        return geography

    def get_response_with_js(self, url: str) -> str:
        response = None
        count = 0
        while response is None and count < 10:
            try:
                count += 1
                session = HTMLSession()
                response = session.get(base_url + url + passthrough_parameters)
                response.html.render()
            except TimeoutError as e:
                print(e)

        if response is None:
            sys.exit("No response from server")

        return response.html.html

    def find_by_var(self, html: str, var: str) -> dict:
        regex = r'var\s*' + var + r'\s*=\s*(.*);'
        result = re.findall(regex, html)[0]
        result = result.replace('\xa0', '')
        parser = JsonComment(json)
        return parser.loads(result)

    def update_overview(self, overview: Overview):
        pass
