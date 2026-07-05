
"""
Volume Analyzer
Version 3.0
"""

import numpy as np


class VolumeAnalyzer:

    def __init__(self, df):

        self.df = df.copy()

    # ==========================
    # میانگین حجم
    # ==========================

    def average_volume(self, period=20):

        return self.df["Volume"].tail(period).mean()

    # ==========================
    # حجم امروز
    # ==========================

    def today_volume(self):

        return float(self.df.iloc[-1]["Volume"])

    # ==========================
    # نسبت حجم
    # ==========================

    def volume_ratio(self):

        avg = self.average_volume()

        if avg == 0:

            return 0

        return round(self.today_volume() / avg, 2)

    # ==========================
    # وضعیت حجم
    # ==========================

    def volume_status(self):

        ratio = self.volume_ratio()

        if ratio >= 3:

            return "بسیار زیاد"

        elif ratio >= 2:

            return "زیاد"

        elif ratio >= 1.2:

            return "بالاتر از میانگین"

        elif ratio >= 0.8:

            return "عادی"

        else:

            return "کم"

    # ==========================
    # افزایش حجم
    # ==========================

    def is_volume_increasing(self):

        v1 = self.df.iloc[-1]["Volume"]
        v2 = self.df.iloc[-2]["Volume"]
        v3 = self.df.iloc[-3]["Volume"]

        return v1 > v2 > v3

    # ==========================
    # کاهش حجم
    # ==========================

    def is_volume_decreasing(self):

        v1 = self.df.iloc[-1]["Volume"]
        v2 = self.df.iloc[-2]["Volume"]
        v3 = self.df.iloc[-3]["Volume"]

        return v1 < v2 < v3

    # ==========================
    # شکست با حجم
    # ==========================

    def breakout_volume(self):

        avg = self.average_volume()

        last = self.today_volume()

        high20 = self.df["High"].tail(20).max()

        close = self.df.iloc[-1]["Close"]

        if last > avg * 2 and close >= high20:

            return True

        return False

    # ==========================
    # امتیاز حجم
    # ==========================

    def score(self):

        ratio = self.volume_ratio()

        if ratio >= 3:

            return 10

        elif ratio >= 2:

            return 8

        elif ratio >= 1.5:

            return 6

        elif ratio >= 1:

            return 4

        return 2

    # ==========================
    # تحلیل
    # ==========================

    def analyze(self):

        return {

            "today_volume": int(self.today_volume()),

            "average_volume": int(self.average_volume()),

            "volume_ratio": self.volume_ratio(),

            "volume_status": self.volume_status(),

            "volume_increasing": self.is_volume_increasing(),

            "volume_decreasing": self.is_volume_decreasing(),

            "breakout_volume": self.breakout_volume(),

            "volume_score": self.score()

        }