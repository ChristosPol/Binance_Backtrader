from binance.client import Client
import pandas as pd
from get_api_keys import *

# Binance API Client constructor
client = Client(api_key, api_secret)

info = client.get_account()
print(info['balances'])

'''
# Get server time in epoch
client.get_server_time()

# System get system status
client.get_system_status()

# System exchange info
client.get_exchange_info()

# Get Symbol info
eth_info=client.get_symbol_info('ETHEUR')
# Attr names
print(eth_info.keys())
print(eth_info['status'])

# Market data endpoints --------------------------------------------------------

# Get market depth (bids and asks)
depth = client.get_order_book(symbol='ETHEUR')
print(pd.DataFrame(depth))
print(depth)
print(type(depth))
print(depth.keys())
print(depth['bids'])
print(depth['asks'])

# Get recent recent trades
trades = client.get_recent_trades(symbol="ETHEUR")
print(pd.DataFrame(trades))

# Get historical DATA
trades = client.get_aggregate_trades(symbol='ETHEUR')
print(pd.DataFrame(trades))

# Aggregate Trade Iterator
agg_trades = client.aggregate_trade_iter(symbol='ETHBTC', start_str='30 minutes ago UTC')
print(pd.DataFrame(agg_trades))

# Get Kline/Candlesticks
candles = client.get_klines(symbol='BNBBTC', interval=Client.KLINE_INTERVAL_30MINUTE)
print(pd.DataFrame(candles))


# Get Historical Kline/Candlesticks
# fetch 1 minute klines for the last day up until now
klines = client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")

# fetch 30 minute klines for the last month of 2017
klines = client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")

# fetch weekly klines since it listed
klines = client.get_historical_klines("NEOBTC", Client.KLINE_INTERVAL_1WEEK, "1 Jan, 2017")

# Get average price for a symbol
avg_price = client.get_avg_price(symbol='ETHEUR')
print(avg_price)

# Get 24hr Ticker
tickers = client.get_ticker(symbol="ETHEUR")
print(tickers)

# Get Orderbook Tickers
tickers = client.get_orderbook_tickers()
print(pd.DataFrame(tickers))

info = client.get_account()
print(info)
'''
