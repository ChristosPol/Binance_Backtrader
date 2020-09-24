from binance.client import Client
import pandas as pd

# Pandas options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Import client api keys
df = pd.read_csv(r'/media/chris/DATA/Documents/Bot_Trading/API_Keys_Binance.txt', sep=";")
api_key = df['API_Key'].to_string()
api_secret = df['API_Sign'].to_string()

# Choose pair
pair = "ETHEUR"

# Binance API Client constructor
client = Client(api_key, api_secret)

# Get historical data for pair and interval
klines = pd.DataFrame(client.get_historical_klines(pair, Client.KLINE_INTERVAL_1HOUR, "60 days ago ECT"))

klines.columns = ["open_time", "Open", "High",
                  "Low", "Close", "Volume",
                  "close_time", "Quote_asset_volume",
                  "N_trades", "Taker_buy_base_asset_volume",
                  "taker_buy_quote_asset_volume", "ignore"]

klines['open_time'] = pd.to_datetime(klines['open_time'], unit='ms')
klines['close_time'] = pd.to_datetime(klines['close_time'], unit='ms')

# Export
klines.to_csv("klines.csv", sep=",")

