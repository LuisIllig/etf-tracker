class Performance:
    def __init__(self, year, total_return, benchmark):
        self.year = year
        self.total_return = total_return
        self.benchmark = benchmark

    def __str__(self):
        return f'Year: {self.year} Total Return: {self.total_return} Benchmark: {self.benchmark}'

    def __repr__(self):
        return self.__str__()


class Portfolio:
    def __init__(self, top_holdings: list[dict[str, int]], exposure: list[str], sector: list[str], geography: list[str]):
        self.top_holdings = top_holdings
        self.exposure = exposure
        self.sector = sector
        self.geography = geography

    def __str__(self):
        return f'Top Holdings: {self.top_holdings} Exposure: {self.exposure} Sector: {self.sector} Geography: {self.geography}'

    def __repr__(self):
        return self.__str__()


class Overview:
    def __init__(self, etf_id: id, performance: list[Performance], portfolio: Portfolio):
        self.id = etf_id
        self.performance = performance
        self.portfolio = portfolio

    def __str__(self):
        return f'ETF: {self.id} Performance: {self.performance} Portfolio: {self.portfolio}'

    def __repr__(self):
        return self.__str__()
