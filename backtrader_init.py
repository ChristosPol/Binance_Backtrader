import backtrader as bt
#import talib as ta
import pandas as pd
import backtrader.indicators as btind
from modules.paths_other import *


class MyStrategy(bt.Strategy):

    def __init__(self):

        self.rsi = bt.indicators.RSI(self.data.close, period=14)


    def next(self):
        if self.rsi < 50 and not self.position:
            # Do something
            self.buy()

        elif self.rsi > 80 and self.position:
            # Do something else
            self.close()

cerebro = bt.Cerebro()
cerebro.broker.setcash(500)
data = bt.feeds.GenericCSVData(dataname=data_path+'ETHEUR365_klines.csv',
                               #dtformat ='%Y-%m-%d %H:%M:%S',
                               datetime = 0,
                               open=1,
                               close=2,
                               high=3,
                               low=4,
                               volume=5,
                               openinterest=-1)
cerebro.adddata(data)
cerebro.addstrategy(MyStrategy)
cerebro.run()
cerebro.plot()
