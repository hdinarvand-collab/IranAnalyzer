"""
ADX Indicator
"""

import ta


class ADXIndicator:

    def __init__(self, df):

        self.df = df.copy()

    def calculate(self):

        indicator = ta.trend.ADXIndicator(

            high=self.df["High"],

            low=self.df["Low"],

            close=self.df["Close"],

            window=14

        )

        self.df["ADX"] = indicator.adx()

        self.df["+DI"] = indicator.adx_pos()

        self.df["-DI"] = indicator.adx_neg()

        return self.df

    def adx(self):

        return round(self.df.iloc[-1]["ADX"],2)

    def plus_di(self):

        return round(self.df.iloc[-1]["+DI"],2)

    def minus_di(self):

        return round(self.df.iloc[-1]["-DI"],2)

    def signal(self):

        adx = self.df.iloc[-1]["ADX"]

        plus = self.df.iloc[-1]["+DI"]

        minus = self.df.iloc[-1]["-DI"]

        if adx < 20:

            return "روند ضعیف"

        if plus > minus:

            return "روند صعودی"

        return "روند نزولی"