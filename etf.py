class Etf:
    def __init__(self, name: str = '', isin: str = '', product_family: str = '', xetra_symbol: str = '',
                 reuters_code: str = '', bloomberg_ticker: str = '', ter: float = 0.0,
                 distribution_policy: str = '', replication_method: str = '', fund_currency: str = '',
                 trading_currency: str = '', inav_reuters: str = '', inav_bloomberg: str = '',
                 benchmark: str = '', homepage: str = ''):
        self.id = f'{isin}_{xetra_symbol}_{reuters_code}_{bloomberg_ticker}'
        self.name = name
        self.isin = isin
        self.product_family = product_family
        self.xetra_symbol = xetra_symbol
        self.reuters_code = reuters_code
        self.bloomberg_ticker = bloomberg_ticker
        self.ter = ter
        self.distribution_policy = distribution_policy
        self.replication_method = replication_method
        self.fund_currency = fund_currency
        self.trading_currency = trading_currency
        self.inav_reuters = inav_reuters
        self.inav_bloomberg = inav_bloomberg
        self.benchmark = benchmark
        self.homepage = homepage

    def __str__(self):
        return f'{self.name} {self.isin}'

    def __repr__(self):
        return f'{self.name} {self.isin}'

    def compare(self, other):
        differences = []
        for key in self.__dict__.keys():
            if self.__dict__[key] != other.__dict__[key]:
                differences.append(key)
        return differences


xls_mapping = {
    'name': 3,
    'isin': 4,
    'product_family': 5,
    'xetra_symbol': 6,
    'reuters_code': 7,
    'bloomberg_ticker': 8,
    'ter': 10,
    'distribution_policy': 11,
    'replication_method': 12,
    'fund_currency': 13,
    'trading_currency': 14,
    'inav_reuters': 17,
    'inav_bloomberg': 18,
    'benchmark': 19,
    'homepage': 20
}


def map_xls(row: tuple) -> Etf:
    return Etf(
        name=row[xls_mapping['name']],
        isin=row[xls_mapping['isin']],
        product_family=row[xls_mapping['product_family']],
        xetra_symbol=row[xls_mapping['xetra_symbol']],
        reuters_code=row[xls_mapping['reuters_code']],
        bloomberg_ticker=row[xls_mapping['bloomberg_ticker']],
        ter=row[xls_mapping['ter']],
        distribution_policy=row[xls_mapping['distribution_policy']],
        replication_method=row[xls_mapping['replication_method']],
        fund_currency=row[xls_mapping['fund_currency']],
        trading_currency=row[xls_mapping['trading_currency']],
        inav_reuters=row[xls_mapping['inav_reuters']],
        inav_bloomberg=row[xls_mapping['inav_bloomberg']],
        benchmark=row[xls_mapping['benchmark']],
        homepage=row[xls_mapping['homepage']]
    )
