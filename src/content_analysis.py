import pandas as pd


def content_analysis(df):

    explicit = (

        df.groupby(

            'is_explicit'

        )

        ['popularity']

        .mean()

        .reset_index()

    )

    album = (

        df.groupby(

            'album_type'

        )

        ['popularity']

        .mean()

        .reset_index()

    )

    duration = (

        df.groupby(

            'song'

        )

        ['duration_min']

        .mean()

        .reset_index()

    )

    return (

        explicit,

        album,

        duration

    )