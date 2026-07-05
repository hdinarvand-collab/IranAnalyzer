
"""
Iran Analyzer
Version 3.0
"""

from analysis.technical import TechnicalAnalyzer
from analysis.fundamental import FundamentalAnalyzer
from analysis.report import ReportGenerator

from analysis.support_resistance import SupportResistanceAnalyzer
from analysis.volume import VolumeAnalyzer
from analysis.smart_money import SmartMoneyAnalyzer
from analysis.divergence import DivergenceAnalyzer
from analysis.patterns import PatternAnalyzer
from analysis.scoring import ScoringEngine

from reports.excel import ExcelReport

from data.prices import PriceLoader
from scanner.market_scanner import MarketScanner


def main():

    print("=" * 50)
    print("        Iran Analyzer V4.0")
    print("=" * 50)

    print("1) تحلیل یک سهم")
    print("2) تحلیل کل بازار")
    print("0) خروج")

    choice = input("\nانتخاب شما : ").strip()

# -------------------------------
# خروج
# -------------------------------
    if choice == "0":
 
     return

# -------------------------------
# تحلیل بازار
# -------------------------------
    if choice == "2":

     scanner = MarketScanner()

     scanner.run()
     return

# -------------------------------
# تحلیل تک سهم
# -------------------------------

    symbol = input("\nنام نماد را وارد کنید : ").strip()

    print("\nدر حال دریافت اطلاعات ...\n")

    # ==========================================
    # دریافت دیتا
    # ==========================================

    loader = PriceLoader(symbol)

    df = loader.load()

    if df is None:

     print("خطا در دریافت اطلاعات.")
    return

    # ==========================================
    # تحلیل تکنیکال
    # ==========================================

    technical = TechnicalAnalyzer(symbol)

    technical_result = technical.run()

    # ==========================================
    # تحلیل بنیادی (فعلاً بدون استفاده)
    # ==========================================

    fundamental = FundamentalAnalyzer(symbol)

    fundamental_result = fundamental.run()

    # ==========================================
    # حمایت و مقاومت
    # ==========================================

    support = SupportResistanceAnalyzer(df)

    support_result = support.analyze()

    # ==========================================
    # حجم
    # ==========================================

    volume = VolumeAnalyzer(df)

    volume_result = volume.analyze()

    # ==========================================
    # پول هوشمند
    # ==========================================

    smart = SmartMoneyAnalyzer(df)

    smart_result = smart.analyze()

    # ==========================================
    # واگرایی
    # ==========================================

    divergence = DivergenceAnalyzer(df)

    divergence_result = divergence.analyze()

    # ==========================================
    # الگوها
    # ==========================================

    pattern = PatternAnalyzer(df)

    pattern_result = pattern.analyze()

    # ==========================================
    # امتیاز نهایی
    # ==========================================

    scoring = ScoringEngine(

        technical_result,

        technical_result,

        support_result,

        volume_result,

        smart_result,

        divergence_result,

        pattern_result

    )

    final_score = scoring.calculate()

    # ==========================================
    # نمایش گزارش
    # ==========================================

    report = ReportGenerator(

        symbol,

        technical_result,

        support_result,

        volume_result,

        smart_result,

        divergence_result,

        pattern_result,

        final_score

    )

    report.show()

    # ==========================================
    # خروجی Excel
    # ==========================================

    excel = ExcelReport(

        symbol,

        technical_result,

        support_result,

        volume_result,

        smart_result,

        divergence_result,

        pattern_result,

        final_score,

        df

    )

    excel.export()


if __name__ == "__main__":

    main()
