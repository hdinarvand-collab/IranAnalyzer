from engines.base_engine import BaseEngine


class DivergenceEngine(BaseEngine):

    def __init__(self, df, rsi_series):
        super().__init__(df)
        self.rsi = rsi_series

    def calculate(self):

        return {
            "divergence_score": 4
        }