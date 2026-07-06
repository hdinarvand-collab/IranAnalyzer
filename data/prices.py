import finpy_tse as tse
import pandas as pd

class PriceLoader:

    def __init__(self, symbol):
        self.symbol = symbol

    def load(self):

        print("Fetching data...")

        try:

            df = tse.Get_Price_History(
                stock=self.symbol,
                start_date="1400-01-01",
                end_date="1404-12-29",
                adjust_price=True
            )

            if df is None or df.empty:
                print("❌ EMPTY DATA")
                return None

            print("Data received:", len(df))
            return df

        except Exception as e:

            print("❌ API ERROR:")
            print(e)

            return None