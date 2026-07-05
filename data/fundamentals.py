"""
Fundamental Data Loader
Version 3.0
"""

from dataclasses import dataclass


@dataclass
class FundamentalData:

    symbol: str

    pe: float | None = None
    eps: float | None = None

    roe: float | None = None
    roa: float | None = None

    market_cap: float | None = None

    float_shares: float | None = None

    dps: float | None = None

    sales_growth: float | None = None

    profit_margin: float | None = None

    debt_ratio: float | None = None


class FundamentalLoader:

    def __init__(self, symbol):

        self.symbol = symbol

    def load(self):

        """
        این متد در نسخه بعدی از API واقعی بورس ایران
        اطلاعات را دریافت خواهد کرد.
        """

        return FundamentalData(
            symbol=self.symbol
        )