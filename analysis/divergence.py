
"""
Divergence Analyzer
Version 3.0
"""

import numpy as np


class DivergenceAnalyzer:

    def __init__(self, df):

        self.df = df.copy()

    # =====================================
    # RSI Divergence
    # =====================================

    def rsi_divergence(self):

        if "RSI" not in self.df.columns:

            return "نامشخص"

        close = self.df["Close"].values
        rsi = self.df["RSI"].values

        p1 = close[-6]
        p2 = close[-1]

        r1 = rsi[-6]
        r2 = rsi[-1]

        # واگرایی مثبت
        if p2 < p1 and r2 > r1:

            return "مثبت"

        # واگرایی منفی
        if p2 > p1 and r2 < r1:

            return "منفی"

        return "ندارد"

    # =====================================
    # MACD Divergence
    # =====================================

    def macd_divergence(self):

        if "MACD" not in self.df.columns:

            return "نامشخص"

        close = self.df["Close"].values
        macd = self.df["MACD"].values

        p1 = close[-6]
        p2 = close[-1]

        m1 = macd[-6]
        m2 = macd[-1]

        # واگرایی مثبت
        if p2 < p1 and m2 > m1:

            return "مثبت"

        # واگرایی منفی
        if p2 > p1 and m2 < m1:

            return "منفی"

        return "ندارد"

    # =====================================
    # امتیاز
    # =====================================

    def score(self):

        score = 0

        if self.rsi_divergence() == "مثبت":

            score += 5

        if self.macd_divergence() == "مثبت":

            score += 5

        if self.rsi_divergence() == "منفی":

            score -= 5

        if self.macd_divergence() == "منفی":

            score -= 5

        return score

    # =====================================
    # تحلیل
    # =====================================

    def analyze(self):

        return {

            "rsi_divergence": self.rsi_divergence(),

            "macd_divergence": self.macd_divergence(),

            "divergence_score": self.score()

        }