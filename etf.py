from pandas import DataFrame


class Etf:
    def __init__(self, name, isin, product_family, xetra_symbol, reuters_code, bloomberg_ticker, ter,
                 distribution_policy, replication_method, fund_currency, trading_currency, inav_reuters, inav_bloomberg,
                 benchmark, homepage):
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


xls_mapping = {
    'name': 'PRODUCT NAME',
    'isin': 'ISIN',
    'product_family': 'PRODUCT FAMILY',
    'xetra_symbol': 'XETRA SYMBOL',
    'reuters_code': 'REUTERS \nCODE',
    'bloomberg_ticker': 'BLOOMBERG TICKER',
    'ter': 'ONGOING CHARGES',
    'distribution_policy': 'USE OF PROFITS',
    'replication_method': 'REPLICATION METHOD',
    'fund_currency': 'FUND CURRENCY',
    'trading_currency': 'TRADING CURRENCY',
    'inav_reuters': 'iNAV (REUTERS)',
    'inav_bloomberg': 'iNAV (BLOOMBERG)',
    'benchmark': 'BENCHMARK',
    'homepage': 'HOMEPAGE ISSUER'
}


def map_xls(df: DataFrame) -> Etf:
    return Etf(
        name=df[xls_mapping['name']],
        isin=df[xls_mapping['isin']],
        product_family=df[xls_mapping['product_family']],
        xetra_symbol=df[xls_mapping['xetra_symbol']],
        reuters_code=df[xls_mapping['reuters_code']],
        bloomberg_ticker=df[xls_mapping['bloomberg_ticker']],
        ter=df[xls_mapping['ter']],
        distribution_policy=df[xls_mapping['distribution_policy']],
        replication_method=df[xls_mapping['replication_method']],
        fund_currency=df[xls_mapping['fund_currency']],
        trading_currency=df[xls_mapping['trading_currency']],
        inav_reuters=df[xls_mapping['inav_reuters']],
        inav_bloomberg=df[xls_mapping['inav_bloomberg']],
        benchmark=df[xls_mapping['benchmark']],
        homepage=df[xls_mapping['homepage']]
    )
