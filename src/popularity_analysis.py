import pandas as pd


def popularity_analysis(df):

    correlation = (

        df['position']

        .corr(

            df['popularity']

        )

    )

    top10 = (

        df[

            df['position'] <= 10

        ]['popularity']

        .mean()

    )

    top20 = (

        df[

            df['position'] <= 20

        ]['popularity']

        .mean()

    )

    top50 = (

        df['popularity']

        .mean()

    )

    return {

        'correlation': correlation,

        'top10': top10,

        'top20': top20,

        'top50': top50

    }