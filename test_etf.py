from etf import Etf, map_xls


def test_compare_equal():
    etf1 = Etf(
        name='test',
        isin='test',
        product_family='test',
        xetra_symbol='test',
        reuters_code='test',
        bloomberg_ticker='test',
        ter='test',
        distribution_policy='test',
        replication_method='test',
        fund_currency='test',
        trading_currency='test',
        inav_reuters='test',
        inav_bloomberg='test',
        benchmark='test',
        homepage='test'
    )
    etf2 = Etf(
        name='test',
        isin='test',
        product_family='test',
        xetra_symbol='test',
        reuters_code='test',
        bloomberg_ticker='test',
        ter='test',
        distribution_policy='test',
        replication_method='test',
        fund_currency='test',
        trading_currency='test',
        inav_reuters='test',
        inav_bloomberg='test',
        benchmark='test',
        homepage='test'
    )
    assert etf1.compare(etf2) == []


def test_compare_diffs():
    etf1 = Etf(
        name='test',
        isin='test',
        product_family='test',
        xetra_symbol='test',
        reuters_code='test',
        bloomberg_ticker='test',
        ter='test',
        distribution_policy='test',
        replication_method='test',
        fund_currency='test',
        trading_currency='test',
        inav_reuters='test',
        inav_bloomberg='test',
        benchmark='test',
        homepage='test'
    )
    etf2 = Etf(
        name='diff',
        isin='test',
        product_family='test',
        xetra_symbol='test',
        reuters_code='test',
        bloomberg_ticker='test',
        ter='test',
        distribution_policy='test',
        replication_method='test',
        fund_currency='test',
        trading_currency='test',
        inav_reuters='test',
        inav_bloomberg='test',
        benchmark='test',
        homepage='diff'
    )
    assert etf1.compare(etf2) == ['name', 'homepage']


def test_map_xls():
    row = list('test' for _ in range(21))
    row[4] = 'isin'
    etf = map_xls(tuple(row))
    assert etf.name == 'test'
    assert etf.isin == 'isin'
