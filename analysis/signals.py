"""
Signal Engine
Version 2.0
"""


class SignalEngine:

    def __init__(self, technical):

        self.tech = technical

    # ==============================
    # روند کلی
    # ==============================

    def trend(self):

        return self.tech["trend"]

    # ==============================
    # RSI
    # ==============================

    def rsi(self):

        value = self.tech["rsi"]

        if value >= 70:
            return "اشباع خرید"

        elif value <= 30:
            return "اشباع فروش"

        elif value >= 50:
            return "صعودی"

        return "نزولی"

    # ==============================
    # EMA
    # ==============================

    def ema(self):

        return self.tech["ema_signal"]

    # ==============================
    # MACD
    # ==============================

    def macd(self):

        return self.tech["macd_status"]

    # ==============================
    # ADX
    # ==============================

    def adx(self):

        return self.tech["adx_signal"]

    # ==============================
    # ICHIMOKU
    # ==============================

    def ichimoku(self):

        return self.tech["ichimoku_signal"]

    # ==============================
    # جمع‌بندی
    # ==============================

    def summary(self):

        return {

            "Trend": self.trend(),

            "RSI": self.rsi(),

            "EMA": self.ema(),

            "MACD": self.macd(),

            "ADX": self.adx(),

            "ICHIMOKU": self.ichimoku()

        }