# Api keys loader
file = open('/media/chris/DATA/Documents/Bot_Trading/API_Keys_Binance.txt', "r")
a = [b.split() for b in file.readlines()]
api_key = str(a[0]).strip('[]').strip("''")
api_secret = str(a[1]).strip('[]').strip("''")
file.close()
