from datetime import datetime

from dotenv import load_dotenv
from iexfinance.refdata import get_symbols
from iexfinance.stocks import get_historical_data
from iexfinance.stocks import Stock

load_dotenv()


start = datetime(2017, 1, 1)
end = datetime(2018, 1, 1)
df = get_historical_data("TSLA", start, end)


aapl = Stock("AAPL", output_format="pandas")
temp = aapl.get_quote()


batch = Stock(["TSLA", "AAPL"])
batch.get_price()


temp = get_symbols()
