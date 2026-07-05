"""
دریافت اطلاعات قیمت سهم
"""

import pandas as pd
import finpy_tse as tse


class PriceLoader:

    def __init__(self, symbol):

        self.symbol = symbol

    def load(self):

        try:

            df = tse.Get_Price_History(

                stock=self.symbol,

                start_date="1400-01-01",

                end_date="1500-01-01",

                ignore_date=True,

                adjust_price=True,

                show_weekday=False,

                double_date=False

            )

            if df is None or len(df) == 0:

                raise Exception("داده‌ای دریافت نشد.")

            # فقط ستون‌های مورد نیاز
            df = df[[
                "Open",
                "High",
                "Low",
                "Close",
                "Final",
                "Volume"
            ]]

            df = df.dropna()

            df.reset_index(drop=True, inplace=True)

            return df

        except Exception as e:

            print("خطا در دریافت اطلاعات:")

            print(e)

            return None