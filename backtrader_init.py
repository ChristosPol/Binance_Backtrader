import backtrader as bt


class RSIStrategy(bt.Strategy):

    def __init__(self):
        self.rsi = bt.indicators.RelativeStrengthIndex(self.data)

    def next(self):
        if self.rsi < 50 and not self.position:
            self.buy(size=1)

        if self.rsi > 70 and self.position:
            self.close()

class MyStrategy(bt.Strategy):

    def __init__(self):
        self.sma = bt.indicators.EMA(period=50)

    def next(self):
        if self.sma > self.data:
            # Do something
            self.buy()

        elif self.sma < self.data:
            # Do something else
            self.close()

cerebro = bt.Cerebro()
cerebro.broker.setcash(500)
data = bt.feeds.GenericCSVData(dataname='klines.csv',
                               timeframe=bt.TimeFrame.Minutes,
                               compression=60,
                               dtformat=2,
                               openinterest=-1)

cerebro.adddata(data)
cerebro.addstrategy(MyStrategy)
cerebro.run()
cerebro.plot()


'''
from datetime import datetime
import backtrader as bt

# Create a subclass of Strategy to define the indicators and logic

class SmaCross(bt.Strategy):
    # list of parameters which are configurable for the strategy
    params = dict(
        pfast=10,  # period for the fast moving average
        pslow=30   # period for the slow moving average
    )

    def __init__(self):
        sma1 = bt.ind.SMA(period=self.p.pfast)  # fast moving average
        sma2 = bt.ind.SMA(period=self.p.pslow)  # slow moving average
        self.crossover = bt.ind.CrossOver(sma1, sma2)  # crossover signal

    def next(self):
        if not self.position:  # not in the market
            if self.crossover > 0:  # if fast crosses slow to the upside
                self.buy()  # enter long

        elif self.crossover < 0:  # in the market & cross to the downside
            self.close()  # close long position


cerebro = bt.Cerebro()  # create a "Cerebro" engine instance

# Create a data feed
data = bt.feeds.YahooFinanceData(dataname='MSFT',
                                 fromdate=datetime(2011, 1, 1),
                                 todate=datetime(2012, 12, 31))

cerebro.adddata(data)  # Add the data feed

cerebro.addstrategy(SmaCross)  # Add the trading strategy
cerebro.run()  # run it all
cerebro.plot()  # and plot it with a single command
'''