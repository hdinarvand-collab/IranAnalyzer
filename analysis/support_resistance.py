
"""
Support & Resistance Engine
Version 3.0
"""

import numpy as np


class SupportResistanceAnalyzer:

    def __init__(self, df):

        self.df = df

    # ==========================
    # Pivot High
    # ==========================

    def pivot_highs(self, left=3, right=3):

        highs = []

        H = self.df["High"].values

        for i in range(left, len(H)-right):

            if H[i] == max(H[i-left:i+right+1]):

                highs.append(H[i])

        return highs

    # ==========================
    # Pivot Low
    # ==========================

    def pivot_lows(self, left=3, right=3):

        lows = []

        L = self.df["Low"].values

        for i in range(left, len(L)-right):

            if L[i] == min(L[i-left:i+right+1]):

                lows.append(L[i])

        return lows

    # ==========================
    # Merge Close Levels
    # ==========================

    def merge_levels(self, levels, percent=1):

        if len(levels) == 0:

            return []

        levels = sorted(levels)

        merged = [levels[0]]

        for level in levels[1:]:

            if abs(level-merged[-1])/merged[-1]*100 < percent:

                merged[-1] = (merged[-1]+level)/2

            else:

                merged.append(level)

        return merged

    # ==========================
    # Analyze
    # ==========================

    def analyze(self):

        close = float(self.df.iloc[-1]["Close"])

        highs = self.pivot_highs()

        lows = self.pivot_lows()

        highs = self.merge_levels(highs)

        lows = self.merge_levels(lows)

        supports = [x for x in lows if x < close]

        resistances = [x for x in highs if x > close]

        supports = sorted(supports, reverse=True)[:3]

        resistances = sorted(resistances)[:3]

        while len(supports) < 3:

            supports.append(None)

        while len(resistances) < 3:

            resistances.append(None)

        if supports[0] is not None:

            support_distance = round(
                (close-supports[0])/close*100,
                2
            )

        else:

            support_distance = None

        if resistances[0] is not None:

            resistance_distance = round(
                (resistances[0]-close)/close*100,
                2
            )

        else:

            resistance_distance = None

        score = 0

        if support_distance is not None:

            if support_distance < 3:

                score += 5

        return {

            "support1": supports[0],
            "support2": supports[1],
            "support3": supports[2],

            "resistance1": resistances[0],
            "resistance2": resistances[1],
            "resistance3": resistances[2],

            "support_distance": support_distance,
            "resistance_distance": resistance_distance,

            "support_score": score

        }
