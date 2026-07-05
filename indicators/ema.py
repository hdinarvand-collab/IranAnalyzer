"""
EMA Indicator
"""

import ta


class EMAIndicator:

    def __init__(self, df):

        self.df = df.copy()

    def calculate(self):

        self.df["EMA20"] = ta.trend.EMAIndicator(
            close=self.df["Close"],
            window=20
        ).ema_indicator()

        self.df["EMA50"] = ta.trend.EMAIndicator(
            close=self.df["Close"],
            window=50
        ).ema_indicator()

        return self.df

    def ema20(self):

        return round(self.df.iloc[-1]["EMA20"], 2)

    def ema50(self):

        return round(self.df.iloc[-1]["EMA50"], 2)

    def signal(self):

        if self.ema20() > self.ema50():
            return "صعودی"

        elif self.ema20() < self.ema50():
            return "نزولی"

        return "خنثی"