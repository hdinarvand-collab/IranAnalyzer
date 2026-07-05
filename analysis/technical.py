
"""
Technical Analysis
Version 3.0
"""

from data.prices import PriceLoader

from indicators.rsi import RSIIndicator
from indicators.ema import EMAIndicator
from indicators.macd import MACDIndicator
from indicators.adx import ADXIndicator
from indicators.ichimoku import IchimokuIndicator

from analysis.trend import TrendAnalyzer


class TechnicalAnalyzer:

    def __init__(self, symbol):

        self.symbol = symbol

    def run(self):

        # ==========================================
        # دریافت اطلاعات قیمت
        # ==========================================

        loader = PriceLoader(self.symbol)

        df = loader.load()

        if df is None or len(df) < 120:

            print("خطا در دریافت اطلاعات قیمت")

            return None

        # ==========================================
        # محاسبه اندیکاتورها
        # ==========================================

        rsi = RSIIndicator(df)
        df = rsi.calculate()

        ema = EMAIndicator(df)
        df = ema.calculate()

        macd = MACDIndicator(df)
        df = macd.calculate()

        adx = ADXIndicator(df)
        df = adx.calculate()

        ichimoku = IchimokuIndicator(df)
        df = ichimoku.calculate()

        # ==========================================
        # داده‌های مورد نیاز Trend Engine
        # ==========================================

        technical = {

            "ema20": ema.ema20(),
            "ema50": ema.ema50(),

            "rsi": rsi.last_value(),

            "macd": macd.macd(),
            "macd_signal": macd.signal_value(),

            "adx": adx.adx(),

            "price_position": ichimoku.price_position(),

            "cloud_color": ichimoku.cloud_color(),

            "future_cloud": ichimoku.future_cloud(),

            "tk_strength": ichimoku.tk_strength(),

            "ichimoku_score": ichimoku.score(),
            


             }

        # ==========================================
        # اجرای Trend Engine
        # ==========================================

        trend_engine = TrendAnalyzer(technical)

        trend = trend_engine.analyze()

        # ==========================================
        # امتیاز اولیه اندیکاتورها
        # ==========================================

        score = 0

        if ema.signal() == "صعودی":
            score += 20

        if rsi.signal() == "صعودی":
            score += 15

        if macd.signal() == "خرید":
            score += 20

        if adx.signal() == "روند صعودی":
            score += 15

        score += int(ichimoku.score() * 0.30)
           

        # اضافه شدن امتیاز Trend Engine
        score += trend["trend_score"]

        # ==========================================
        # خروجی
        # ==========================================

        result = {

            # روند
            "trend": trend["trend"],
            "short_trend": trend["short_trend"],
            "mid_trend": trend["mid_trend"],
            "long_trend": trend["long_trend"],
            "trend_strength": trend["trend_strength"],
            "market_state": trend["market_state"],
            "trend_score": trend["trend_score"],

            # عمومی
            "rows": len(df),
            "last_close": int(df.iloc[-1]["Close"]),

            # RSI
            "rsi": rsi.last_value(),
            "rsi_signal": rsi.signal(),

            # EMA
            "ema20": ema.ema20(),
            "ema50": ema.ema50(),
            "ema_signal": ema.signal(),

            # MACD
            "macd": macd.macd(),
            "macd_signal": macd.signal_value(),
            "macd_histogram": macd.histogram(),
            "macd_status": macd.signal(),

            # ADX
            "adx": adx.adx(),
            "plus_di": adx.plus_di(),
            "minus_di": adx.minus_di(),
            "adx_signal": adx.signal(),

            # Ichimoku
            "tenkan": ichimoku.tenkan(),
            "kijun": ichimoku.kijun(),
            "span_a": ichimoku.span_a(),
            "span_b": ichimoku.span_b(),
            "chikou": ichimoku.chikou(),

            "cloud_color": ichimoku.cloud_color(),

            "cloud_thickness": ichimoku.cloud_thickness(),

            "cloud_slope": ichimoku.cloud_slope(),

            "future_cloud": ichimoku.future_cloud(),

            "future_twist": ichimoku.future_twist(),




            "price_position": ichimoku.price_position(),

            "distance_to_cloud": ichimoku.distance_to_cloud(),



            "tk_cross": ichimoku.tk_cross(),

            "tk_strength": ichimoku.tk_strength(),

            "tk_distance": ichimoku.tk_distance(),

            "chikou_status": ichimoku.chikou_status(),

            "trend_continuation": ichimoku.trend_continuation(),

            "reversal_risk": ichimoku.reversal_risk(),

            "ichimoku_score": ichimoku.score(),

            "ichimoku_signal": ichimoku.signal(),

            # امتیاز
            "score": score

        }

        return result

