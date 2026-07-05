"""
Market Scanner
Version 1.0
"""

import pandas as pd

from analysis.technical import TechnicalAnalyzer
from scanner.ranking import Ranking


class MarketScanner:

    def __init__(self):

        self.symbols_file = "data/symbols.xlsx"

        self.results = []

    # ==========================================
    # خواندن لیست نمادها
    # ==========================================

    def load_symbols(self):

        try:

            df = pd.read_excel(self.symbols_file)

            return df

        except Exception as e:

            print()

            print("خطا در خواندن فایل نمادها")

            print(e)

            return None

    # ==========================================
    # اسکن بازار
    # ==========================================

    def run(self):

        df = self.load_symbols()

        if df is None:

            return

        total = len(df)

        print()
        print("=" * 60)
        print("شروع اسکن بازار")
        print("=" * 60)
        print()

        counter = 1

        for _, row in df.iterrows():

            symbol = str(row["Symbol"]).strip()

            print(f"[{counter}/{total}] {symbol}")

            try:

                analyzer = TechnicalAnalyzer(symbol)

                result = analyzer.run()

                if result is None:

                    counter += 1

                    continue

                score = result.get("score", 0)

                trend = result.get("trend", "")

                self.results.append({

                    "symbol": symbol,

                    "score": score,

                    "trend": trend,

                    "price": result.get("last_close", 0),

                    "rsi": result.get("rsi", 0),

                    "macd": result.get("macd_status", ""),

                    "ichimoku": result.get("ichimoku_signal", "")

                })

                print(f"      Score : {score}")

            except Exception as e:

                print("      Error :", e)

            counter += 1

        # ======================================
        # مرتب سازی
        # ======================================

        top10 = Ranking.top10(self.results)

        print()
        print("=" * 60)
        print("TOP 10 MARKET")
        print("=" * 60)

        rank = 1

        for item in top10:

            print(

                f"{rank:2} - "

                f"{item['symbol']:10}"

                f" Score : {item['score']:3}"

                f" Trend : {item['trend']}"

            )

            rank += 1

        print()

        return top10