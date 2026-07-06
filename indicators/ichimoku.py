import pandas as pd
from indicators.base import BaseIndicator


class IchimokuIndicator(BaseIndicator):

    def __init__(self, df):
        super().__init__(df)

        self.high = df["High"]
        self.low = df["Low"]
        self.close = df["Close"]

    def calculate(self):
        return self.close

    def price_position(self):

        if self.close.iloc[-1] > self.close.mean():
            return "بالای ابر"
        return "پایین ابر"

    def cloud_color(self):
        return "صعودی"

    def tk_cross(self):
        return "صعودی"