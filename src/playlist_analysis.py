import pandas as pd


def playlist_analysis(df):

    daily_distribution = (

        df.groupby('date')

        ['position']

        .mean()

        .reset_index()

    )

    fast_risers = (

        df.groupby('song')

        ['position']

        .agg(

            ['max', 'min']

        )

        .reset_index()

    )

    fast_risers['rank_change'] = (

        fast_risers['max']

        -

        fast_risers['min']

    )

    fast_risers = (

        fast_risers

        .sort_values(

            'rank_change',

            ascending=False

        )

        .head(10)

    )

    return daily_distribution, fast_risers