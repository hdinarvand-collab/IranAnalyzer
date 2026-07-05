
"""
Report Generator
Version 3.0
"""


class ReportGenerator:

    def __init__(
        self,
        symbol,
        technical,
        support=None,
        volume=None,
        smart_money=None,
        divergence=None,
        pattern=None,
        final_score=None
    ):

        self.symbol = symbol
        self.technical = technical
        self.support = support or {}
        self.volume = volume or {}
        self.smart_money = smart_money or {}
        self.divergence = divergence or {}
        self.pattern = pattern or {}
        self.final_score = final_score or {}

    # ==========================================
    # چاپ گزارش
    # ==========================================

    def show(self):

        print("\n")
        print("=" * 60)
        print(f"        گزارش تحلیل {self.symbol}")
        print("=" * 60)

        print(f"\nآخرین قیمت : {self.technical['last_close']}")

        # ======================================
        # روند
        # ======================================

        print("\n" + "-" * 60)
        print("روند بازار")
        print("-" * 60)

        print("روند کوتاه مدت :", self.technical["short_trend"])
        print("روند میان مدت :", self.technical["mid_trend"])
        print("روند بلند مدت :", self.technical["long_trend"])
        print("قدرت روند :", self.technical["trend_strength"])
        print("وضعیت بازار :", self.technical["market_state"])

        # ======================================
        # اندیکاتورها
        # ======================================

        print("\n" + "-" * 60)
        print("اندیکاتورها")
        print("-" * 60)

        print("RSI :", self.technical["rsi"])
        print("RSI Signal :", self.technical["rsi_signal"])

        print("EMA20 :", self.technical["ema20"])
        print("EMA50 :", self.technical["ema50"])

        print("MACD :", self.technical["macd"])
        print("MACD Signal :", self.technical["macd_status"])

        print("ADX :", self.technical["adx"])
        print("ADX Signal :", self.technical["adx_signal"])

        print("Ichimoku :", self.technical["price_position"])

        # ======================================
        # حمایت و مقاومت
        # ======================================

        if self.support:

            print("\n" + "-" * 60)
            print("حمایت و مقاومت")
            print("-" * 60)

            print("Support1 :", self.support.get("support1"))
            print("Support2 :", self.support.get("support2"))
            print("Support3 :", self.support.get("support3"))

            print()

            print("Resistance1 :", self.support.get("resistance1"))
            print("Resistance2 :", self.support.get("resistance2"))
            print("Resistance3 :", self.support.get("resistance3"))

            print()

            print("Distance To Support :", self.support.get("support_distance"), "%")
            print("Distance To Resistance :", self.support.get("resistance_distance"), "%")

        # ======================================
        # حجم
        # ======================================

        if self.volume:

            print("\n" + "-" * 60)
            print("حجم معاملات")
            print("-" * 60)

            print("Volume Ratio :", self.volume.get("volume_ratio"))
            print("Volume Status :", self.volume.get("volume_status"))
            print("Volume Score :", self.volume.get("volume_score"))

        # ======================================
        # پول هوشمند
        # ======================================

        if self.smart_money:

            print("\n" + "-" * 60)
            print("پول هوشمند")
            print("-" * 60)

            print("Money Flow :", self.smart_money.get("money_flow"))
            print("Money Strength :", self.smart_money.get("money_strength"))
            print("Money Power :", self.smart_money.get("money_power"))

        # ======================================
        # واگرایی
        # ======================================

        if self.divergence:

            print("\n" + "-" * 60)
            print("واگرایی")
            print("-" * 60)

            print("RSI :", self.divergence.get("rsi_divergence"))
            print("MACD :", self.divergence.get("macd_divergence"))

        # ======================================
        # الگو
        # ======================================

        if self.pattern:

            print("\n" + "-" * 60)
            print("الگو")
            print("-" * 60)

            print("Pattern :", self.pattern.get("pattern"))

        # ======================================
        # امتیاز نهایی
        # ======================================

        if self.final_score:

            print("\n" + "=" * 60)
            print("نتیجه نهایی")
            print("=" * 60)

            print("Final Score :", self.final_score.get("final_score"), "/100")
            print("Signal :", self.final_score.get("signal"))

        print("\n")

    # ==========================================
    # Excel
    # ==========================================

    def export_excel(self):

        print("-" * 60)
        print("گزارش Excel ذخیره شد.")
        print("output\\{}_analysis.xlsx".format(self.symbol))
        print("-" * 60)