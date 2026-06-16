import pandas as pd


def artist_analysis(df):

    artist_stats = (

        df.groupby('artist')

        .agg(

            unique_songs=(

                'song',

                'nunique'

            ),

            total_days=(

                'date',

                'nunique'

            )

        )

        .reset_index()

    )

    artist_stats = (

        artist_stats

        .sort_values(

            'unique_songs',

            ascending=False

        )

    )

    return artist_stats