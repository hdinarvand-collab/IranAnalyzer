"""
Relative Strength Index (RSI)
"""

import ta


class RSIIndicator:

    def __init__(self, df):

        self.df = df.copy()

    def calculate(self):

        self.df["RSI"] = ta.momentum.RSIIndicator(
            close=self.df["Close"],
            window=14
        ).rsi()

        return self.df

    def last_value(self):

        value = self.df["RSI"].iloc[-1]

        return round(value, 2)

    def signal(self):

        value = self.last_value()

        if value < 30:
            return "اشباع فروش"

        elif value > 70:
            return "اشباع خرید"

        elif value >= 50:
            return "صعودی"

        else:
            return "نزولی"