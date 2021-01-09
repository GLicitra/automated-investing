import plotly.graph_objects as go
from plotly.subplots import make_subplots


def candlestick(df, ticker):
    fig = go.Figure()
    # go.Figure()
    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        # vertical_spacing=0.02,
        specs=[
            [{"secondary_y": True}],
            # [{"secondary_y": True}, {"secondary_y": True}],
            [{"secondary_y": True}],
        ]
        #                    specs=[[{"secondary_x": True},{"secondary_x": True}],
        #                    [{"secondary_x": True},{"secondary_x": True}],
        #                    [{"secondary_x": True},{"secondary_x": True}]]
    )

    fig.add_trace(
        go.Candlestick(
            x=df.index,
            open=df.open,
            high=df.high,
            low=df.low,
            close=df.close,
            name="Price",
            increasing_line_color="#93c47d",
            decreasing_line_color="#e06666",
        ),
        row=1,
        col=1,
        secondary_y=False,
    )

    INCREASING_COLOR = "#008000"  # green
    DECREASING_COLOR = "#ff0000"  # red
    colors = []
    for i in range(len(df.close)):
        if i != 0:
            if df.close[i] > df.open[i]:
                colors.append(INCREASING_COLOR)
            else:
                colors.append(DECREASING_COLOR)
        else:
            colors.append(DECREASING_COLOR)
    fig.add_trace(
        go.Bar(x=df.index, y=df.volume, name="Vplume", marker=dict(color=colors)),
        row=2,
        col=1,
        secondary_y=True,
    )
    """
    fig.add_trace(go.Bar(x=df.sip_timestamp,
                         y=df.taker_buy_base_asset_volume,
                         name='taker_buy on ask',
                         marker=dict(color=INCREASING_COLOR, opacity=0.5, line_color='rgb(8,48,107)', line_width=1)),
                  row=1, col=1, secondary_y=True)
    fig.add_trace(go.Bar(x=df.sip_timestamp,
                         y=df.volume - df.taker_buy_base_asset_volume,
                         name='taker_sell on bid',
                         marker=dict(color=DECREASING_COLOR, opacity=0.5, line_color='rgb(8,48,107)', line_width=1)),
                  row=1, col=1, secondary_y=True)

    fig.update_layout(barmode='group')
    """
    """
    fig.add_trace(go.Bar(x=df.time,
                      y=df.volume,
                      name='Volume',
                      marker=dict( color=colors, opacity=0.1, line_color='rgb(8,48,107)', line_width=2 )),
                      row=1, col=1, secondary_y=True)
    """
    fig.update_layout(
        # barmode='group',
        xaxis={"type": "category"},
        title=ticker + " price (USD)",
        paper_bgcolor="white",
        plot_bgcolor="whitesmoke",
    )
    fig["layout"]["yaxis1"] = dict(domain=[0.5, 1.0])  # Price
    fig["layout"]["yaxis4"] = dict(domain=[0.0, 0.3])  # Volume

    return fig.show()


def candlestick_bid_ask(df, ticker):
    # fig = go.Figure()
    fig = make_subplots(
        rows=3,
        cols=2,
        shared_xaxes=True,
        # vertical_spacing=0.02,
        specs=[
            [{"secondary_y": True}, {"secondary_y": True}],
            [{"secondary_y": True}, {"secondary_y": True}],
            [{"secondary_y": True}, {"secondary_y": True}],
        ]
        # specs=[[{"secondary_x": True},{"secondary_x": True}],[{"secondary_x": True},{"secondary_x": True}],[{"secondary_x": True},{"secondary_x": True}]]
    )

    fig.add_trace(
        go.Candlestick(
            x=df.index,
            open=df.open,
            high=df.high,
            low=df.low,
            close=df.close,
            name="Price",
            increasing_line_color="#93c47d",
            decreasing_line_color="#e06666",
        ),
        row=1,
        col=1,
        secondary_y=False,
    )

    INCREASING_COLOR = "#008000"  # green
    DECREASING_COLOR = "#ff0000"  # red
    colors = []
    for i in range(len(df.close)):
        if i != 0:
            if df.close[i] > df.open[i]:
                colors.append(INCREASING_COLOR)
            else:
                colors.append(DECREASING_COLOR)
        else:
            colors.append(DECREASING_COLOR)

    fig.add_trace(
        go.Bar(
            x=df.index,
            y=df.most_on_ask,
            name="ton ask",
            marker=dict(
                color=INCREASING_COLOR,
                opacity=0.5,
                line_color="rgb(8,48,107)",
                line_width=1,
            ),
        ),
        row=1,
        col=1,
        secondary_y=True,
    )
    fig.add_trace(
        go.Bar(
            x=df.index,
            y=df.most_on_bid,
            name="on bid",
            marker=dict(
                color=DECREASING_COLOR,
                opacity=0.5,
                line_color="rgb(8,48,107)",
                line_width=1,
            ),
        ),
        row=1,
        col=1,
        secondary_y=True,
    )

    fig.update_layout(barmode="group")
    """
    fig.add_trace(go.Bar(x=df.time,
                      y=df.volume,
                      name='Volume',
                      marker=dict( color=colors, opacity=0.1, line_color='rgb(8,48,107)', line_width=2 )),
                      row=1, col=1, secondary_y=True)
    """
    fig.update_layout(
        # barmode='group',
        xaxis={"type": "category"},
        title=ticker + " price (USD)",
        paper_bgcolor="white",
        plot_bgcolor="whitesmoke",
    )

    return fig.show()
