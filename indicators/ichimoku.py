"""
Ichimoku Cloud Professional V2
"""

import pandas as pd
import numpy as np


class IchimokuIndicator:

    def __init__(self, df):

        self.df = df.copy()

    # ==========================================
    # Calculate
    # ==========================================

    def calculate(self):

        high9 = self.df["High"].rolling(9).max()
        low9 = self.df["Low"].rolling(9).min()

        self.df["TENKAN"] = (high9 + low9) / 2

        high26 = self.df["High"].rolling(26).max()
        low26 = self.df["Low"].rolling(26).min()

        self.df["KIJUN"] = (high26 + low26) / 2

        self.df["SPAN_A"] = (
            (
                self.df["TENKAN"] +
                self.df["KIJUN"]
            ) / 2
        ).shift(26)

        high52 = self.df["High"].rolling(52).max()
        low52 = self.df["Low"].rolling(52).min()

        self.df["SPAN_B"] = (
            (
                high52 +
                low52
            ) / 2
        ).shift(26)

        self.df["CHIKOU"] = (
            self.df["Close"]
        ).shift(-26)

        return self.df

    # ==========================================
    # Base Values
    # ==========================================

    def tenkan(self):

        return round(self.df.iloc[-1]["TENKAN"],2)

    def kijun(self):

        return round(self.df.iloc[-1]["KIJUN"],2)

    def span_a(self):

        return round(self.df.iloc[-27]["SPAN_A"],2)

    def span_b(self):

        return round(self.df.iloc[-27]["SPAN_B"],2)

    def chikou(self):

        return round(self.df.iloc[-27]["CHIKOU"],2)
        # ==========================================
    # Cloud Color
    # ==========================================

    def cloud_color(self):

        span_a = self.df.iloc[-27]["SPAN_A"]
        span_b = self.df.iloc[-27]["SPAN_B"]

        if pd.isna(span_a) or pd.isna(span_b):
            return "نامشخص"

        if span_a > span_b:
            return "ابر صعودی"

        elif span_a < span_b:
            return "ابر نزولی"

        return "خنثی"

    # ==========================================
    # Cloud Thickness
    # ==========================================

    def cloud_thickness(self):

        span_a = self.df.iloc[-27]["SPAN_A"]
        span_b = self.df.iloc[-27]["SPAN_B"]

        if pd.isna(span_a) or pd.isna(span_b):
            return "نامشخص"

        thickness = abs(span_a - span_b)

        close = self.df.iloc[-1]["Close"]

        percent = thickness / close * 100

        if percent < 1:
            return "بسیار نازک"

        elif percent < 2:
            return "نازک"

        elif percent < 4:
            return "متوسط"

        elif percent < 7:
            return "ضخیم"

        return "بسیار ضخیم"

    # ==========================================
    # Cloud Slope
    # ==========================================

    def cloud_slope(self):

        span_a_now = self.df.iloc[-27]["SPAN_A"]
        span_a_old = self.df.iloc[-37]["SPAN_A"]

        if pd.isna(span_a_now) or pd.isna(span_a_old):
            return "نامشخص"

        diff = span_a_now - span_a_old

        if diff > 0:
            return "صعودی"

        elif diff < 0:
            return "نزولی"

        return "خنثی"

    # ==========================================
    # Future Cloud
    # ==========================================

    def future_cloud(self):

        span_a = self.df.iloc[-1]["SPAN_A"]
        span_b = self.df.iloc[-1]["SPAN_B"]

        if pd.isna(span_a) or pd.isna(span_b):
            return "نامشخص"

        if span_a > span_b:
            return "آینده صعودی"

        elif span_a < span_b:
            return "آینده نزولی"

        return "خنثی"

    # ==========================================
    # Future Twist
    # ==========================================

    def future_twist(self):

        span_a1 = self.df.iloc[-2]["SPAN_A"]
        span_b1 = self.df.iloc[-2]["SPAN_B"]

        span_a2 = self.df.iloc[-1]["SPAN_A"]
        span_b2 = self.df.iloc[-1]["SPAN_B"]

        if pd.isna(span_a1) or pd.isna(span_b1):
            return "نامشخص"

        if (span_a1 < span_b1) and (span_a2 > span_b2):
            return "Bullish Twist"

        if (span_a1 > span_b1) and (span_a2 < span_b2):
            return "Bearish Twist"

        return "بدون Twist"
        # ==========================================
    # Price Position
    # ==========================================

    def price_position(self):

        close = self.df.iloc[-1]["Close"]

        span_a = self.df.iloc[-27]["SPAN_A"]
        span_b = self.df.iloc[-27]["SPAN_B"]

        if pd.isna(span_a) or pd.isna(span_b):
            return "نامشخص"

        top = max(span_a, span_b)
        bottom = min(span_a, span_b)

        if close > top:
            return "بالای ابر"

        elif close < bottom:
            return "پایین ابر"

        return "داخل ابر"

    # ==========================================
    # Distance To Cloud
    # ==========================================

    def distance_to_cloud(self):

        close = self.df.iloc[-1]["Close"]

        span_a = self.df.iloc[-27]["SPAN_A"]
        span_b = self.df.iloc[-27]["SPAN_B"]

        if pd.isna(span_a) or pd.isna(span_b):
            return None

        top = max(span_a, span_b)
        bottom = min(span_a, span_b)

        if close > top:
            distance = ((close - top) / close) * 100

        elif close < bottom:
            distance = ((bottom - close) / close) * 100

        else:
            distance = 0

        return round(distance, 2)

    # ==========================================
    # TK Cross
    # ==========================================

    def tk_cross(self):

        tenkan_now = self.df.iloc[-1]["TENKAN"]
        kijun_now = self.df.iloc[-1]["KIJUN"]

        tenkan_prev = self.df.iloc[-2]["TENKAN"]
        kijun_prev = self.df.iloc[-2]["KIJUN"]

        if pd.isna(tenkan_now) or pd.isna(kijun_now):
            return "نامشخص"

        if tenkan_prev <= kijun_prev and tenkan_now > kijun_now:
            return "کراس صعودی"

        elif tenkan_prev >= kijun_prev and tenkan_now < kijun_now:
            return "کراس نزولی"

        elif tenkan_now > kijun_now:
            return "صعودی"

        elif tenkan_now < kijun_now:
            return "نزولی"

        return "خنثی"

    # ==========================================
    # TK Cross Strength
    # ==========================================

    def tk_strength(self):

        cross = self.tk_cross()

        position = self.price_position()

        if cross == "کراس صعودی":

            if position == "بالای ابر":
                return "بسیار قوی"

            elif position == "داخل ابر":
                return "متوسط"

            return "ضعیف"

        elif cross == "کراس نزولی":

            if position == "پایین ابر":
                return "بسیار قوی"

            elif position == "داخل ابر":
                return "متوسط"

            return "ضعیف"

        return "بدون کراس"

    # ==========================================
    # TK Distance
    # ==========================================

    def tk_distance(self):

        tenkan = self.df.iloc[-1]["TENKAN"]
        kijun = self.df.iloc[-1]["KIJUN"]

        if pd.isna(tenkan) or pd.isna(kijun):
            return None

        distance = abs(tenkan - kijun)

        percent = (distance / self.df.iloc[-1]["Close"]) * 100

        return round(percent, 2)
        # ==========================================
    # Chikou Status
    # ==========================================

    def chikou_status(self):

        try:

            chikou = self.df.iloc[-27]["CHIKOU"]

            price = self.df.iloc[-27]["Close"]

            span_a = self.df.iloc[-27]["SPAN_A"]
            span_b = self.df.iloc[-27]["SPAN_B"]

            if pd.isna(chikou):
                return "نامشخص"

            top = max(span_a, span_b)
            bottom = min(span_a, span_b)

            if chikou > price:

                if chikou > top:
                    return "بالای قیمت و ابر"

                return "بالای قیمت"

            else:

                if chikou < bottom:
                    return "پایین قیمت و ابر"

                return "پایین قیمت"

        except:

            return "نامشخص"

    # ==========================================
    # Trend Continuation
    # ==========================================

    def trend_continuation(self):

        score = 0

        if self.price_position() == "بالای ابر":
            score += 25

        if self.cloud_color() == "ابر صعودی":
            score += 20

        if self.future_cloud() == "آینده صعودی":
            score += 15

        if self.tk_cross() in ["صعودی", "کراس صعودی"]:
            score += 20

        if "بالای" in self.chikou_status():
            score += 20

        if score >= 80:
            return "بسیار زیاد"

        elif score >= 60:
            return "زیاد"

        elif score >= 40:
            return "متوسط"

        return "ضعیف"

    # ==========================================
    # Reversal Risk
    # ==========================================

    def reversal_risk(self):

        risk = 0

        if self.distance_to_cloud() is not None:

            if self.distance_to_cloud() > 8:
                risk += 30

            elif self.distance_to_cloud() > 5:
                risk += 20

        if self.tk_distance() is not None:

            if self.tk_distance() > 5:
                risk += 20

        if self.cloud_thickness() == "بسیار نازک":
            risk += 20

        if self.future_twist() != "بدون Twist":
            risk += 20

        if risk >= 70:
            return "بسیار زیاد"

        elif risk >= 50:
            return "زیاد"

        elif risk >= 30:
            return "متوسط"

        return "کم"

    # ==========================================
    # Ichimoku Score
    # ==========================================

    def score(self):

        score = 0

        if self.price_position() == "بالای ابر":
            score += 20

        if self.cloud_color() == "ابر صعودی":
            score += 15

        if self.future_cloud() == "آینده صعودی":
            score += 10

        if self.tk_strength() == "بسیار قوی":
            score += 20

        elif self.tk_strength() == "متوسط":
            score += 10

        if "بالای" in self.chikou_status():
            score += 15

        if self.cloud_thickness() in ["ضخیم", "بسیار ضخیم"]:
            score += 10

        if self.cloud_slope() == "صعودی":
            score += 10

        return min(score, 100)
    
    # ==========================================
    # Backward Compatibility
    # ==========================================

    def strength(self):
        return self.tk_strength()

    # ==========================================
    # Final Signal
    # ==========================================

    def signal(self):

        score = self.score()

        if score >= 85:
            return "خرید بسیار قوی"

        elif score >= 70:
            return "خرید"

        elif score >= 55:
            return "مثبت"

        elif score >= 40:
            return "خنثی"

        elif score >= 25:
            return "منفی"

        return "فروش"