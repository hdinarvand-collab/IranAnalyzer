import pandas as pd
from indicators.base import BaseIndicator


class MACDIndicator(BaseIndicator):

    def __init__(self, df):
        super().__init__(df)
        self.close = df["Close"]

        self.macd_line, self.signal_line, self.hist = self._calculate()

    def _calculate(self):

        ema12 = self.close.ewm(span=12, adjust=False).mean()
        ema26 = self.close.ewm(span=26, adjust=False).mean()

        macd = ema12 - ema26
        signal = macd.ewm(span=9, adjust=False).mean()
        hist = macd - signal

        return macd, signal, hist

    def calculate(self):
        return self.macd_line

    def macd(self):
        return self.macd_line.iloc[-1]

    def signal_value(self):
        return self.signal_line.iloc[-1]

    def histogram_value(self):
        return self.hist.iloc[-1]

    def status(self):

        if self.hist.iloc[-1] > 0:
            return "خرید"
        return "فروش"