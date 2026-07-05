"""
MACD Indicator
"""

import ta


class MACDIndicator:

    def __init__(self, df):

        self.df = df.copy()

    def calculate(self):

        indicator = ta.trend.MACD(
            close=self.df["Close"],
            window_fast=12,
            window_slow=26,
            window_sign=9
        )

        self.df["MACD"] = indicator.macd()
        self.df["MACD_SIGNAL"] = indicator.macd_signal()
        self.df["MACD_HIST"] = indicator.macd_diff()

        return self.df

    def macd(self):

        return round(self.df.iloc[-1]["MACD"], 2)

    def signal_value(self):

        return round(self.df.iloc[-1]["MACD_SIGNAL"], 2)

    def histogram(self):

        return round(self.df.iloc[-1]["MACD_HIST"], 2)

    def signal(self):

        macd = self.df.iloc[-1]["MACD"]
        signal = self.df.iloc[-1]["MACD_SIGNAL"]

        if macd > signal:
            return "خرید"

        elif macd < signal:
            return "فروش"

        return "خنثی"
