"""
Fundamental Analyzer
"""

from data.fundamentals import FundamentalLoader


class FundamentalAnalyzer:

    def __init__(self, symbol):

        self.symbol = symbol

    def run(self):

        data = FundamentalLoader(self.symbol).load()

        score = 0

        # PE

        if data.pe is not None:

            if data.pe < 8:

                score += 25

            elif data.pe < 12:

                score += 15

        # ROE

        if data.roe is not None:

            if data.roe > 25:

                score += 25

            elif data.roe > 15:

                score += 15

        # Profit Margin

        if data.profit_margin is not None:

            if data.profit_margin > 20:

                score += 25

        # Sales Growth

        if data.sales_growth is not None:

            if data.sales_growth > 10:

                score += 25

        return {

            "pe": data.pe,

            "eps": data.eps,

            "roe": data.roe,

            "roa": data.roa,

            "market_cap": data.market_cap,

            "float_shares": data.float_shares,

            "dps": data.dps,

            "sales_growth": data.sales_growth,

            "profit_margin": data.profit_margin,

            "debt_ratio": data.debt_ratio,

            "score": score

        }