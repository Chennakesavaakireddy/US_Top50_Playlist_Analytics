import pandas as pd


def create_features(df):

    # Duration in minutes

    df['duration_min'] = round(
        df['duration_ms'] / 60000,
        2
    )

    # Days on chart

    days = (
        df.groupby('song')['date']
        .nunique()
        .reset_index()
    )

    days.columns = [
        'song',
        'days_on_chart'
    ]

    df = df.merge(
        days,
        on='song',
        how='left'
    )

    # Average rank

    avg_rank = (
        df.groupby('song')['position']
        .mean()
        .reset_index()
    )

    avg_rank.columns = [
        'song',
        'avg_rank'
    ]

    df = df.merge(
        avg_rank,
        on='song'
    )

    # Best rank

    best_rank = (
        df.groupby('song')['position']
        .min()
        .reset_index()
    )

    best_rank.columns = [
        'song',
        'best_rank'
    ]

    df = df.merge(
        best_rank,
        on='song'
    )

    # Rank volatility

    volatility = (
        df.groupby('song')['position']
        .std()
        .reset_index()
    )

    volatility.columns = [
        'song',
        'rank_volatility'
    ]

    df = df.merge(
        volatility,
        on='song'
    )

    # Popularity trend

    df = df.sort_values('date')

    df['popularity_trend'] = (
        df.groupby('song')['popularity']
        .transform(
            lambda x:
            x.rolling(
                7,
                min_periods=1
            ).mean()
        )
    )

    return df