"""
Trend Engine
Version 3.0
"""

class TrendAnalyzer:

    def __init__(self, technical):

        self.t = technical

    def analyze(self):

        score = 0

        # ==========================
        # Short Trend
        # ==========================

        if (
            self.t["ema20"] > self.t["ema50"]
            and self.t["macd"] > self.t["macd_signal"]
            and self.t["rsi"] > 50
        ):

            short = "صعودی"
            score += 5

        elif (
            self.t["ema20"] < self.t["ema50"]
            and self.t["macd"] < self.t["macd_signal"]
            and self.t["rsi"] < 50
        ):

            short = "نزولی"

        else:

            short = "خنثی"

        # ==========================
        # Mid Trend
        # ==========================

        if self.t["ema20"] > self.t["ema50"]:

            mid = "صعودی"
            score += 5

        elif self.t["ema20"] < self.t["ema50"]:

            mid = "نزولی"

        else:

            mid = "خنثی"

        # ==========================
        # Long Trend
        # ==========================

        if self.t["price_position"] == "بالای ابر":

            long = "صعودی"
            score += 5

        elif self.t["price_position"] == "پایین ابر":

            long = "نزولی"

        else:

            long = "خنثی"

        # ==========================
        # Trend Strength
        # ==========================

        adx = self.t["adx"]

        if adx is None:

            strength = "نامشخص"

        elif adx < 20:

            strength = "ضعیف"

        elif adx < 25:

            strength = "متوسط"
            score += 1

        elif adx < 40:

            strength = "قوی"
            score += 3

        else:

            strength = "بسیار قوی"
            score += 5

        # ==========================
        # Market State
        # ==========================

        if adx is not None and adx < 20:

            market = "رنج"

        else:

            market = "رونددار"

        # ==========================
        # Final Trend
        # ==========================

        if short == mid == long == "صعودی":

            final = "صعودی"

        elif short == mid == long == "نزولی":

            final = "نزولی"

        else:

            final = "خنثی"

        return {

            "trend": final,

            "short_trend": short,

            "mid_trend": mid,

            "long_trend": long,

            "trend_strength": strength,

            "market_state": market,

            "trend_score": score

        }