from binance.client import Client
import pandas as pd
import sys
from get_api_keys import *

# Choose pair
# pair = "ETHEUR"
# backperiod = "365"

pair = sys.argv[1]
backperiod = str(sys.argv[2])

print("Downloading data for " + pair + " for the last " +backperiod+ " days")

# Binance API Client constructor
client = Client(api_key, api_secret)

# Get historical data for pair and interval
klines = pd.DataFrame(client.get_historical_klines(pair,
                                                   Client.KLINE_INTERVAL_1HOUR,
                                                   backperiod+" days ago ECT"))

klines.columns = ["open_time", "Open", "High",
                  "Low", "Close", "Volume",
                  "close_time", "Quote_asset_volume",
                  "N_trades", "Taker_buy_base_asset_volume",
                  "taker_buy_quote_asset_volume", "ignore"]
klines_exp = klines[["open_time", "close_time", "Open", "Close", "High", "Low", "Volume"]]

# Export
klines_exp.to_csv(pair+backperiod+"_"+"klines.csv", sep=",", index=False)

print("Export complete")
