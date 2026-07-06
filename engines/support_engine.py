from engines.base_engine import BaseEngine


class SupportEngine(BaseEngine):

    def calculate(self):

        return {
            "support_score": 6
        }