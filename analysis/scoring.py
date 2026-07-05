
"""
Scoring Engine
Version 3.0
"""


class ScoringEngine:

    def __init__(
        self,
        technical,
        trend,
        support,
        volume,
        smart_money,
        divergence,
        pattern
    ):

        self.technical = technical
        self.trend = trend
        self.support = support
        self.volume = volume
        self.smart_money = smart_money
        self.divergence = divergence
        self.pattern = pattern

    # ===========================================
    # محاسبه امتیاز
    # ===========================================

    def calculate(self):

        score = 0

        # -----------------------------
        # Trend
        # -----------------------------

        score += self.trend.get("trend_score", 0)

        # -----------------------------
        # RSI
        # -----------------------------

        if self.technical["rsi_signal"] == "صعودی":

            score += 8

        # -----------------------------
        # EMA
        # -----------------------------

        if self.technical["ema_signal"] == "صعودی":

            score += 10

        # -----------------------------
        # MACD
        # -----------------------------

        if self.technical["macd_status"] == "خرید":

            score += 10

        # -----------------------------
        # ADX
        # -----------------------------

        if self.technical["adx_signal"] == "روند صعودی":

            score += 8

        # -----------------------------
        # Ichimoku
        # -----------------------------

        if self.technical["price_position"] == "بالای ابر":

            score += 12

        # -----------------------------
        # Support
        # -----------------------------

        score += self.support.get("support_score", 0)

        # -----------------------------
        # Volume
        # -----------------------------

        score += self.volume.get("volume_score", 0)

        # -----------------------------
        # Smart Money
        # -----------------------------

        score += self.smart_money.get("smart_money_score", 0)

        # -----------------------------
        # Divergence
        # -----------------------------

        score += self.divergence.get("divergence_score", 0)

        # -----------------------------
        # Pattern
        # -----------------------------

        score += self.pattern.get("pattern_score", 0)

        # -----------------------------
        # محدود کردن امتیاز
        # -----------------------------

        if score > 100:

            score = 100

        if score < 0:

            score = 0

        # -----------------------------
        # نتیجه
        # -----------------------------

        if score >= 85:

            signal = "خرید بسیار قوی"

        elif score >= 70:

            signal = "خرید"

        elif score >= 55:

            signal = "نگهداری"

        elif score >= 40:

            signal = "ضعیف"

        else:

            signal = "فروش"

        return {

            "final_score": score,

            "signal": signal

        }