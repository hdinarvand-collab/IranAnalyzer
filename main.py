from data.prices import PriceLoader
from analysis.technical import TechnicalAnalyzer
from reports.excel import ExcelReport


def main():

    print("=" * 50)
    print("        Iran Analyzer V5.0")
    print("=" * 50)

    print("1) تحلیل یک سهم")
    print("2) تحلیل کل بازار")
    print("0) خروج")

    choice = input("\nانتخاب شما : ")

    if choice != "1":
        print("فعلاً فقط تحلیل تک سهم فعال است")
        return

    symbol = input("\nنام نماد را وارد کنید : ")

    print("\nدر حال دریافت اطلاعات ...")

    # ======================================
    # 1) LOAD DATA
    # ======================================
    loader = PriceLoader(symbol)
    df = loader.load()

    if df is None or len(df) == 0:
        print("❌ خطا در دریافت دیتا")
        return

    print("✔ دیتا دریافت شد:", len(df))

    # ======================================
    # 2) TECHNICAL ANALYSIS
    # ======================================
    print("\nدر حال تحلیل تکنیکال ...")

    technical = TechnicalAnalyzer(symbol).run()

    print("✔ تحلیل تکنیکال انجام شد")

    # ======================================
    # 3) EXCEL REPORT
    # ======================================
    print("\nدر حال ساخت Excel ...")

    try:

        excel = ExcelReport(
            symbol=symbol,
            technical=technical,
            support={},
            volume={},
            smart_money={},
            divergence={},
            pattern={},
            final_score=technical,
            df=df
        )

        excel.export()

        print("✔ Excel ساخته شد")

    except Exception as e:

        print("❌ Excel Error:")
        print(e)


if __name__ == "__main__":
    main()