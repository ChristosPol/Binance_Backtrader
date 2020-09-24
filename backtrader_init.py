import backtrader as bt

class RSIStrategy(bt.Strategy):

    def __init__(self):
        self.rsi = bt.indicators.RelativeStrengthIndex(self.data,  period=5)

    def next(self):
        if self.rsi < 45 and not self.position:
            self.buy(size=1)

        if self.rsi > 70 and self.position:
            self.close()

cerebro = bt.Cerebro()
cerebro.broker.setcash(500)
data = bt.feeds.GenericCSVData(dataname='klines.csv',
                               timeframe=bt.TimeFrame.Minutes,
                               compression=60,
                               dtformat=2,
                               #datetime=0,
                               #high=1,
                               #low=2,
                               #open=3,
                               #close=4,
                               #volume=5,
                               openinterest=-1)

cerebro.adddata(data)
cerebro.addstrategy(RSIStrategy)
cerebro.run()
cerebro.plot()
