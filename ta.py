import pandas as pd
import datetime
import matplotlib.pyplot as plt
pd.set_option('display.max_column',None)
pd.set_option('display.max_rows',None)

data = pd.read_csv("ETHEUR365_klines.csv")

data['open_time'] = data['open_time']/1000.0
data['close_time'] = data['close_time']/1000.0

data['open_time'] = data['open_time'].apply(lambda x: datetime.datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S.%f'))
data['close_time'] = data['close_time'].apply(lambda x: datetime.datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S.%f'))

data["SMA1"] = data['Close'].rolling(window=50).mean()
data["SMA2"] = data['Close'].rolling(window=200).mean()
data['middle_band'] = data['Close'].rolling(window=20).mean()
data['upper_band'] = data['Close'].rolling(window=20).mean() + data['Close'].rolling(window=20).std()*2
data['lower_band'] = data['Close'].rolling(window=20).mean() - data['Close'].rolling(window=20).std()*2


plt.figure(figsize=(10,10))
plt.plot(data['Close'], label ="Close")
plt.plot(data['SMA1'], 'g--', label="SMA1")
plt.plot(data['SMA2'], 'r--', label="SMA2")
plt.plot(data['upper_band'], 'g--', label="upper")
plt.plot(data['middle_band'], 'r--', label="middle")
plt.plot(data['lower_band'], 'y--', label="lower")
plt.legend()
plt.show()
