
"""
Patterns Analyzer
Version 3.0
"""

import numpy as np


class PatternAnalyzer:

    def __init__(self, df):

        self.df = df.copy()

    # =====================================
    # Double Bottom
    # =====================================

    def double_bottom(self):

        low = self.df["Low"].tail(40).values

        p1 = np.argmin(low[:20])
        p2 = np.argmin(low[20:]) + 20

        l1 = low[p1]
        l2 = low[p2]

        if abs(l1 - l2) / max(l1, l2) < 0.03:

            return True

        return False

    # =====================================
    # Double Top
    # =====================================

    def double_top(self):

        high = self.df["High"].tail(40).values

        p1 = np.argmax(high[:20])
        p2 = np.argmax(high[20:]) + 20

        h1 = high[p1]
        h2 = high[p2]

        if abs(h1 - h2) / max(h1, h2) < 0.03:

            return True

        return False

    # =====================================
    # Ascending Trend
    # =====================================

    def ascending_channel(self):

        close = self.df["Close"].tail(20).values

        x = np.arange(len(close))

        slope = np.polyfit(x, close, 1)[0]

        return slope > 0

    # =====================================
    # Descending Trend
    # =====================================

    def descending_channel(self):

        close = self.df["Close"].tail(20).values

        x = np.arange(len(close))

        slope = np.polyfit(x, close, 1)[0]

        return slope < 0

    # =====================================
    # Triangle
    # =====================================

    def triangle(self):

        high = self.df["High"].tail(30)

        low = self.df["Low"].tail(30)

        h_slope = np.polyfit(range(len(high)), high, 1)[0]
        l_slope = np.polyfit(range(len(low)), low, 1)[0]

        if h_slope < 0 and l_slope > 0:

            return True

        return False

    # =====================================
    # نام الگو
    # =====================================

    def pattern_name(self):

        if self.double_bottom():

            return "کف دوقلو"

        if self.double_top():

            return "سقف دوقلو"

        if self.triangle():

            return "مثلث"

        if self.ascending_channel():

            return "کانال صعودی"

        if self.descending_channel():

            return "کانال نزولی"

        return "الگوی خاصی یافت نشد"

    # =====================================
    # امتیاز
    # =====================================

    def score(self):

        name = self.pattern_name()

        if name == "کف دوقلو":

            return 10

        if name == "کانال صعودی":

            return 8

        if name == "مثلث":

            return 6

        if name == "سقف دوقلو":

            return -8

        if name == "کانال نزولی":

            return -6

        return 0

    # =====================================
    # تحلیل
    # =====================================

    def analyze(self):

        return {

            "pattern": self.pattern_name(),

            "pattern_score": self.score()

        }