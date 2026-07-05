
"""
Smart Money Analyzer
Version 3.0
"""

import numpy as np


class SmartMoneyAnalyzer:

    def __init__(self, df):

        self.df = df.copy()

    # ======================================
    # حجم امروز
    # ======================================

    def today_volume(self):

        return float(self.df.iloc[-1]["Volume"])

    # ======================================
    # میانگین حجم
    # ======================================

    def average_volume(self, period=20):

        return self.df["Volume"].tail(period).mean()

    # ======================================
    # ارزش معاملات
    # ======================================

    def traded_value(self):

        close = float(self.df.iloc[-1]["Close"])

        volume = float(self.df.iloc[-1]["Volume"])

        return close * volume

    # ======================================
    # قدرت پول
    # ======================================

    def money_power(self):

        avg = self.average_volume()

        if avg == 0:

            return 0

        ratio = self.today_volume() / avg

        return round(ratio, 2)

    # ======================================
    # ورود یا خروج پول
    # ======================================

    def money_flow(self):

        close_today = self.df.iloc[-1]["Close"]
        close_yesterday = self.df.iloc[-2]["Close"]

        ratio = self.money_power()

        if close_today > close_yesterday and ratio >= 2:

            return "ورود پول"

        if close_today < close_yesterday and ratio >= 2:

            return "خروج پول"

        return "خنثی"

    # ======================================
    # قدرت ورود
    # ======================================

    def strength(self):

        ratio = self.money_power()

        if ratio >= 3:

            return "بسیار قوی"

        elif ratio >= 2:

            return "قوی"

        elif ratio >= 1.5:

            return "متوسط"

        elif ratio >= 1:

            return "ضعیف"

        else:

            return "بسیار ضعیف"

    # ======================================
    # امتیاز
    # ======================================

    def score(self):

        flow = self.money_flow()

        strength = self.strength()

        if flow == "ورود پول":

            if strength == "بسیار قوی":

                return 10

            elif strength == "قوی":

                return 8

            elif strength == "متوسط":

                return 6

            else:

                return 4

        if flow == "خروج پول":

            return 0

        return 2

    # ======================================
    # تحلیل
    # ======================================

    def analyze(self):

        return {

            "money_flow": self.money_flow(),

            "money_strength": self.strength(),

            "money_power": self.money_power(),

            "traded_value": int(self.traded_value()),

            "smart_money_score": self.score()

        }