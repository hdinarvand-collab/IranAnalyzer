import numpy as np
import pandas as pd
from indicators.base import BaseIndicator


class RSIIndicator(BaseIndicator):

    def __init__(self, df, period=14):
        super().__init__(df)
        self.period = period
        self.close = df["Close"]
        self.rsi = self._calculate()

    def _calculate(self):

        delta = self.close.diff()

        gain = np.where(delta > 0, delta, 0)
        loss = np.where(delta < 0, -delta, 0)

        gain = pd.Series(gain, index=self.df.index)
        loss = pd.Series(loss, index=self.df.index)

        avg_gain = gain.rolling(self.period).mean()
        avg_loss = loss.rolling(self.period).mean()

        rs = avg_gain / (avg_loss + 1e-10)

        rsi = 100 - (100 / (1 + rs))

        return rsi.fillna(50)

    def calculate(self):
        return self.rsi

    def value(self):
        return float(self.rsi.iloc[-1])

    def series(self):
        return self.rsi

    def signal(self):

        v = self.value()

        if v > 70:
            return "فروش"
        elif v < 30:
            return "خرید"
        return "خنثی"