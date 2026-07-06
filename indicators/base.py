class BaseIndicator:

    def __init__(self, df):
        self.df = df

    def calculate(self):
        raise NotImplementedError("calculate() must be implemented")

    def value(self):
        return None

    def series(self):
        return None

    def signal(self):
        return "neutral"