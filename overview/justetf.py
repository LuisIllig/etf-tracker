import time

from etf import Etf
from overview.overview import *
from overview.overview_scrapper import OverviewScrapper
from pymongo.database import Database

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

base_url = 'https://www.justetf.com/'
product = 'en/etf-profile.html?isin='


class JustETF(OverviewScrapper):
    def __init__(self, etf: Etf, db: Database):
        super().__init__(etf, db)

    def get_overview(self, dryrun: bool = False):
        print(self.etf.isin)
        driver = None
        try:
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                       firefox_profile=webdriver.FirefoxProfile('firefox-profile/z56p2qif.selenium'))
            driver.get(base_url + product + self.etf.isin)
            time.sleep(10)
            cookies = driver.find_elements(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection')
            if len(cookies) > 0:
                cookies[0].click()
            elements = driver.find_elements(By.XPATH, "//*[@class='expand-link d-inline-block p-2']")
            # press element to open the table
            for element in elements:
                element.click()
            container = driver.find_element(By.XPATH, "//div[@class='constituents-countries']")
            # get parent div from container
            container = container.find_element(By.XPATH, "./..")
            tables = container.find_elements(By.TAG_NAME, 'table')
            for table in tables:
                rows = table.find_elements(By.TAG_NAME, 'tr')
                for row in rows:
                    cols = row.find_elements(By.TAG_NAME, 'td')
                    print(cols[0].text)
                    print(cols[1].text)
        except Exception as e:
            print(e)
        finally:
            if driver is not None:
                driver.quit()
