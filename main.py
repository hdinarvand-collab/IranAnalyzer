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

    # ======================================
    # 1) TECHNICAL ANALYSIS (شامل دریافت دیتا)
    # ======================================
    print("\nدر حال دریافت اطلاعات و تحلیل تکنیکال ...")

    result = TechnicalAnalyzer(symbol).run()

    if result is None:
        print("❌ خطا در دریافت اطلاعات یا تحلیل تکنیکال")
        return

    df = result["df"]

    print("✔ دیتا دریافت شد:", len(df))
    print("✔ تحلیل تکنیکال انجام شد")

    # ======================================
    # 2) EXCEL REPORT
    # ======================================
    print("\nدر حال ساخت Excel ...")

    try:

        excel = ExcelReport(
            symbol=symbol,
            technical=result["technical"],
            support=result["support"],
            volume=result["volume"],
            smart_money=result["smart_money"],
            divergence=result["divergence"],
            pattern=result["pattern"],
            final_score=result["final_score"],
            df=df
        )

        excel.export()

        print("✔ Excel ساخته شد")

    except Exception as e:

        print("❌ Excel Error:")
        print(e)


if __name__ == "__main__":
    main()