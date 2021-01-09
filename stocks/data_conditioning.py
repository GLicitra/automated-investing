# import numpy as np
# import pandas as pd
#
#
# def compute_volume_bid_ask(aggs: pd.DataFrame, df_OHLCV: pd.DataFrame):
#
#     aggs_OHLCV_vol_true = df_OHLCV.resample(rule="1Min")[
#         ["most_on_bid", "volume"]
#     ].apply(lambda x: x.loc[x["most_on_bid"] == True, "volume"].sum())
#     aggs_OHLCV_vol_true.name = "most_on_bid"
#     aggs_OHLCV_vol_true = aggs_OHLCV_vol_true.to_frame()
#
#     aggs_OHLCV_vol_false = df_OHLCV.resample(rule="1Min")[
#         ["most_on_bid", "volume"]
#     ].apply(lambda x: x.loc[x["most_on_bid"] == False, "volume"].sum())
#     aggs_OHLCV_vol_false.name = "most_on_ask"
#     aggs_OHLCV_vol_false = aggs_OHLCV_vol_false.to_frame()
#
#     aggs = aggs.merge(
#         aggs_OHLCV_vol_true, left_index=True, right_index=True, how="inner"
#     )
#
#     aggs = aggs.merge(
#         aggs_OHLCV_vol_false, left_index=True, right_index=True, how="inner"
#     )
#     return aggs
#
#
# def construct_OHLCV(df: pd.DataFrame):
#     """
#     compute OHLCV
#     TODO: add docstring
#     :param df:
#     :return: pd.Series
#     """
#     nan_ptc = df["price"].isna().sum() / df["price"].shape[0]
#
#     # remove any row with NaNs
#     # _ = df.dropna(axis="index", how="any", inplace=True)
#     if not df.empty:
#         df_OHLCV = pd.Series(
#             data={
#                 "open": df["price"].iloc[0],  # Open price
#                 "high": df["price"].max(),  # High price
#                 "low": df["price"].min(),  # Low price
#                 "close": df["price"].iloc[-1],  # Close price
#                 "volume": df["size"].sum(),  # Volume
#                 "most_on_bid": True
#                 if df["price"].iloc[0] > df["price"].iloc[-1]
#                 else False,  # if open > close then bid else
#             }
#         )
#     else:
#         df_OHLCV = pd.Series(
#             data={
#                 "open": np.nan,  # Open price
#                 "high": np.nan,  # High price
#                 "low": np.nan,  # Low price
#                 "close": np.nan,  # Close price
#                 "volume": np.nan,  # Volume
#                 "most_on_bid": np.nan,  # if open > close then bid else
#             }
#         )
#
#     return df_OHLCV
