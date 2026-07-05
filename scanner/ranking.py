"""
Ranking Engine
Version 1.0
"""


class Ranking:

    @staticmethod
    def sort(results):

        return sorted(

            results,

            key=lambda x: x["score"],

            reverse=True

        )

    # ======================================
    # TOP 10
    # ======================================

    @staticmethod
    def top10(results):

        return Ranking.sort(results)[:10]

    # ======================================
    # TOP 20
    # ======================================

    @staticmethod
    def top20(results):

        return Ranking.sort(results)[:20]

    # ======================================
    # TOP 50
    # ======================================

    @staticmethod
    def top50(results):

        return Ranking.sort(results)[:50]

    # ======================================
    # حداقل امتیاز
    # ======================================

    @staticmethod
    def min_score(results, score=70):

        return [

            item

            for item in results

            if item["score"] >= score

        ]

    # ======================================
    # فقط روند صعودی
    # ======================================

    @staticmethod
    def bullish(results):

        return [

            item

            for item in results

            if item["trend"] == "صعودی"

        ]

    # ======================================
    # چاپ نتایج
    # ======================================

    @staticmethod
    def show(results):

        print()

        print("=" * 60)

        print("رتبه‌بندی بازار")

        print("=" * 60)

        rank = 1

        for item in results:

            print(

                f"{rank:2} | "

                f"{item['symbol']:10} | "

                f"Score : {item['score']:3} | "

                f"{item['trend']}"

            )

            rank += 1

        print()