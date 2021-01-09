# import matplotlib.pyplot as plt
# import pandas as pd
# import pyodbc
# import seaborn as sns
#
# import stocks.plot_functions as pp
# import stocks.polygon_data_functions as pf
# from stocks.data_conditioning import compute_volume_bid_ask
# from stocks.data_conditioning import construct_OHLCV
#
#
# pd.set_option("display.max_rows", 50)
# pd.set_option("display.max_columns", 50)
# pd.set_option("display.width", 100)
#
# # ticker = 'CLSN' #shitty biotech penny stock
# ticker = "SPY"  # sp500 Spyder ETF
# date = "2020-07-06"
# hour_init = "09:30:00"
# hour_end = "9:40:00"
#
# aggs = pf.historic_agg(ticker, date, hour_init, hour_end)  # candles
# print("historic aggs", aggs)
# print("Day volume", aggs["volume"].sum())
# print("average minute volume", aggs["volume"].sum() * 0.00256410256)
# aggs.to_csv("aggs.csv")
# pp.candlestick(aggs, ticker)
#
# quotes = pf.historic_quotes(ticker, date, hour_init, hour_end)
# print("historic quotes", quotes)
# print("total ask volume", quotes["ask_size"].sum())
# print("total bid volume", quotes["bid_size"].sum())
# quotes.to_csv("quotes.csv")
#
# trades = pf.historic_trades(ticker, date, hour_init, hour_end)
# print("historic trades", trades)
# print("trades volume", trades["size"].sum())
# trades.to_csv("trades.csv")
#
# # aggregate for each second
# ts_trades = "5S"
# df_OHLCV = trades.resample(rule=ts_trades)[["size", "price"]].apply(construct_OHLCV)
# print("OHLCV aggs", df_OHLCV)
# pp.candlestick(df_OHLCV, ticker)
#
# OHLCV_bid_ask = compute_volume_bid_ask(aggs, df_OHLCV)
# print("OHLCV_bid_ask", OHLCV_bid_ask)
# # df_OHLCV.to_csv('df_OHLCV.csv')
# pp.candlestick_bid_ask(OHLCV_bid_ask, ticker)
#
# plt.figure(1)
# plt.hist(quotes.bid_price, weights=quotes.bid_size, label="bid", bins=40)
# plt.hist(quotes.ask_price, weights=quotes.ask_size, label="ask", bins=40)
# plt.legend(loc="upper left")
# plt.figure(2)
# plt.hist(trades.price, weights=trades["size"], bins=40)
# # plt.figure(3)
# # sns.pairplot(trades)
# plt.show()
#
#
# # Creating and writing data to a local SQL server
# driver = "{ODBC Driver 17 for SQL Server}"
# server = "TUE016408\SQLEXPRESS"
# database = "stock_database"  # You need to create it in advance in Microsoft SQL server management studio
# conn = pyodbc.connect(
#     "Driver="
#     + driver
#     + "; \
#                       Server="
#     + server
#     + "; \
#                       Database="
#     + database
#     + "; \
#                       InitialCatalog=dbo; \
#                       Trusted_Connection=yes;"
# )
# # creating the connection cursor
# cursor = conn.cursor()
# insert_trades = (
#     """INSERT INTO trades(date_time, exchange, size, price) VALUES(?,?,?,?)"""
# )
#
# # uncomment when you run first time, or when you write into SQL
# """
# # create table dbo.trades
# cursor.execute('create table trades(date_time datetime, exchange integer, size integer, price float)')
# conn.commit()
#
# # insert data in batch
# trades.insert(0, 'date_time', trades.index) # I had to add new datetime column in front, otherwise SQL doesnt write index
# print('trades', trades)
# cursor.fast_executemany = True
# for row_count in range(0, trades.shape[0]): # Check this: https://medium.com/analytics-vidhya/speed-up-bulk-inserts-to-sql-db-using-pandas-and-python-61707ae41990
#    chunk = trades.iloc[row_count:row_count + 1, :].values.tolist()
#    tuple_of_tuples = tuple(tuple(x) for x in chunk)
#    cursor.executemany(insert_trades, tuple_of_tuples)
# conn.commit()
# """
#
# # read from SQL (writing needs sqlalchemy package, but seems that pyodbc works fast and fine)
# SQL_read = pd.read_sql("SELECT * FROM trades", conn)
# print("SQL_read", SQL_read)
#
# # insert data by row
# # data_records = (trades.exchange, trades.size, trades.price)
# # crsr.execute(insert_records, data_records)
#
# # TODO 1) Remove NaNs (Yeah, I think we dont really need them when we will analyze data, you are right)
# # Next I will focus on TODO 2 and TODO 4.
# # TODO 2) Accumulate trades @ 5m interval using for loop (10 minutes is already close to the limit of 50000 trades per call)
# # TODO 3) BACKTEST: find significant price moves and see what was happening with traded Volume (threshold volume V_th, V_bid/V_ask) over the average range between these price moves
# # TODO 4) pull live data from the socket and try to enter/exit simple trades in paper stocks account
# # TODO 5) We can write the function for QuantPro Api (Trading 212) that enters the trade based on Polygon socket data
# # TODO 6) Azure/AWS server with SQL, CPU and virtual machine for robust algo execution
