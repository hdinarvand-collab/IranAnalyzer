from data.prices import PriceLoader

from indicators.rsi import RSIIndicator
from indicators.ema import EMAIndicator
from indicators.macd import MACDIndicator
from indicators.adx import ADXIndicator
from indicators.ichimoku import IchimokuIndicator

from engines.support_engine import SupportEngine
from engines.volume_engine import VolumeEngine
from engines.smart_money_engine import SmartMoneyEngine
from engines.divergence_engine import DivergenceEngine
from engines.pattern_engine import PatternEngine

from analysis.trend import TrendAnalyzer


class TechnicalAnalyzer:

    def __init__(self, symbol):
        self.symbol = symbol

    def run(self):

        # =========================
        # LOAD DATA
        # =========================

        df = PriceLoader(self.symbol).load()

        if df is None or len(df) < 50:
            print("خطا در دریافت اطلاعات")
            return None

        # =========================
        # INDICATORS
        # =========================

        rsi = RSIIndicator(df)

        ema = EMAIndicator(df)
        ema.calculate()

        macd = MACDIndicator(df)
        macd.calculate()

        adx = ADXIndicator(df)
        adx.calculate()

        ichimoku = IchimokuIndicator(df)
        ichimoku.calculate()

        # =========================
        # ENGINE LAYER
        # =========================

        support = SupportEngine(df).calculate()
        volume = VolumeEngine(df).calculate()
        smart_money = SmartMoneyEngine(df).calculate()
        divergence = DivergenceEngine(df, rsi.series()).calculate()
        pattern = PatternEngine(df).calculate()

        # =========================
        # SAFE TECHNICAL DICT
        # =========================

        technical = {

            # RSI
            "rsi": rsi.value(),
            "rsi_signal": rsi.signal(),

            # EMA (FIXED ORDER - NO ERROR)
            "ema20": ema.ema20(),
            "ema50": ema.ema50(),
            "ema_signal": ema.signal(),

            # MACD
            "macd": macd.macd(),
            "macd_signal": macd.signal_value(),
            "macd_histogram": macd.histogram_value(),
            "macd_status": macd.status(),

            # ADX
            "adx": adx.adx(),
            "adx_signal": adx.signal(),

            # ICHIMOKU
            "price_position": ichimoku.price_position(),
            "cloud_color": ichimoku.cloud_color(),
            "tk_cross": ichimoku.tk_cross()
        }

        # =========================
        # TREND ANALYSIS (SAFE)
        # =========================

        trend_engine = TrendAnalyzer(technical)
        trend = trend_engine.analyze()

        technical.update(trend)

        # =========================
        # FINAL SCORE
        # =========================

        final_score = {
            "final_score": (
                support["support_score"] +
                volume["volume_score"] +
                smart_money["smart_money_score"] +
                divergence["divergence_score"] +
                pattern["pattern_score"] +
                30
            ),
            "signal": "خرید"
        }

        return {
            "technical": technical,
            "support": support,
            "volume": volume,
            "smart_money": smart_money,
            "divergence": divergence,
            "pattern": pattern,
            "final_score": final_score,
            "df": df
        }