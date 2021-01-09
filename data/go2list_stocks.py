r"""
Title: Go-to-list stocks
Description: list of stocks which can be monitored by default
"""
from pandas import DataFrame

go2list_dict = {
    "ticker": [
        "AAPL",
        "BABA",
        "FB",
        "NFLX",
        "GS",
        "NVDA",
        "SVXY",
        "TNA",
        "SPY",
        "TVIX",
    ],
    "company-name": [
        "Apple Inc.",
        "Alibaba Group Holding Ltd",
        "Facebook, Inc.",
        "Netflix Inc",
        "Goldman Sachs Group Inc",
        "NVIDIA Corporation",
        "PROSHARES TR II/SHORT VIX SHORT-TER",
        "DIREXION SHS ET/SMALL CAP BULL 3X S",
        "SPDR S&P 500 ET/TR UT",
        "VelocityShares Daily 2x VIX Short-Term ETN",
    ],
    "index-listed": [
        "NASDAQ",
        "HKG",
        "NASDAQ",
        "NASDAQ",
        "NYSE",
        "NASDAQ",
        "NYSEARCA",
        "NYSEARCA",
        "NYSEARCA",
        "INDEXCBOE",
    ],
}

go2list = DataFrame(data=go2list_dict)
