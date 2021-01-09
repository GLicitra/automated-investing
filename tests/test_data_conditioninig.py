import numpy as np
import pandas as pd

a = np.array(
    [
        1457392827660434006,
        1457392828660434012,
        1457392829660434023,
        1457474706167386148,
        1457474706167386520,
        1457474706167387512,
        1457474706167452112,
    ]
)


pd.to_datetime(a, unit="ns").values


key_ID = "PKPWA2WEB4VYFN0LH6KX"
Secret_key = "fLxGB9xjsIqbgJ0Rpz/yvb5ji5U0ADlOVDDNNDeU"
# api = tradeapi.REST(key_ID, Secret_key, api_version="v2")


def historic_trades(ticker, date, start, end):
    full_date = date + " " + start
    full_date_end = date + " " + end
    st = dt.datetime.strptime(full_date, "%Y-%m-%d %H:%M:%S")
    st_end = dt.datetime.strptime(full_date_end, "%Y-%m-%d %H:%M:%S")
    st = timezone("US/Eastern").localize(st)
    st_end = timezone("US/Eastern").localize(st_end)
    st = int(st.timestamp()) * 1e9
    st_end = int(st_end.timestamp()) * 1e9
    df = api.polygon.historic_trades_v2(
        ticker, date, timestamp=int(st), timestamp_limit=int(st_end)
    ).df
    df = df.drop(
        columns={
            "trf_timestamp",
            "sequence_number",
            "id",
            "conditions",
            "participant_timestamp",
            "tape",
        },
        axis=1,
    )
    return df
