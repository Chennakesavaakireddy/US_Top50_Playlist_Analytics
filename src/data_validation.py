import pandas as pd


def load_and_validate(filepath):

    df = pd.read_csv(filepath)

    print("Dataset Loaded")

    # Convert date

    df['date'] = pd.to_datetime(
        df['date'],
        errors='coerce'
    )

    # Standardize artist names

    df['artist'] = (
        df['artist']
        .astype(str)
        .str.strip()
        .str.title()
    )

    # Missing values

    missing = df.isnull().sum()

    print("\nMissing Values")

    print(missing)

    # Duplicate song-date entries

    duplicates = df.duplicated(
        subset=['date', 'song']
    ).sum()

    print("\nDuplicate Song-Date Entries")

    print(duplicates)

    # Rank validation

    invalid_rank = df[
        (df['position'] < 1)
        | (df['position'] > 50)
    ]

    print("\nInvalid Rank Rows")

    print(len(invalid_rank))

    # Remove duplicates

    df = df.drop_duplicates(
        subset=['date', 'song']
    )

    return df