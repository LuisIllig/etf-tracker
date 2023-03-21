class Performance:
    def __init__(self, year, total_return, benchmark):
        self.year = year
        self.total_return = total_return
        self.benchmark = benchmark

    def __str__(self):
        return f'Year: {self.year} Total Return: {self.total_return} Benchmark: {self.benchmark}'

    def __repr__(self):
        return self.__str__()


class Position:
    def __init__(self, ticker: str, name: str, sector: str, _type: str, weight: float):
        self.ticker = ticker
        self.name = name
        self.sector = sector
        self.type = _type
        self.weight = weight

    def __str__(self):
        return f'Ticker: {self.ticker} Name: {self.name} Sector: {self.sector} Type: {self.type} Weight: {self.weight}'

    def __repr__(self):
        return self.__str__()


class Sector:
    def __init__(self, category: str, fonds: int):
        self.category = category
        self.fonds = fonds

    def __str__(self):
        return f'Category: {self.category} Fonds: {self.fonds}'

    def __repr__(self):
        return self.__str__()


class Geography:
    def __init__(self, country: str, fonds: int):
        self.country = country
        self.fonds = fonds

    def __str__(self):
        return f'Country: {self.country} Fonds: {self.fonds}'

    def __repr__(self):
        return self.__str__()


class Portfolio:
    def __init__(self, positions: list[Position], sector: list[Sector], geography: list[Geography]):
        self.positions = positions
        self.sector = sector
        self.geography = geography

    def __str__(self):
        return f'Top Holdings: {self.positions} Sector: {self.sector} Geography: {self.geography}'

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
