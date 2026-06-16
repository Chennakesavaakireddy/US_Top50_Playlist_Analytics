import pandas as pd


def song_analysis(df):

    summary = (

        df.groupby('song')

        .agg(

            days_on_chart=(

                'date',

                'nunique'

            ),

            avg_popularity=(

                'popularity',

                'mean'

            ),

            best_rank=(

                'position',

                'min'

            )

        )

        .reset_index()

    )

    longest_presence = (

        summary

        .sort_values(

            'days_on_chart',

            ascending=False

        )

        .head(10)

    )

    highest_popularity = (

        summary

        .sort_values(

            'avg_popularity',

            ascending=False

        )

        .head(10)

    )

    return (

        longest_presence,

        highest_popularity

    )