from src.data_validation import load_and_validate

from src.feature_engineering import create_features

from src.playlist_analysis import playlist_analysis

from src.song_analysis import song_analysis

from src.artist_analysis import artist_analysis

from src.popularity_analysis import popularity_analysis

from src.content_analysis import content_analysis

import os

# ------------------------

# CREATE OUTPUT FOLDER

# ------------------------

os.makedirs("output", exist_ok=True)

# ------------------------

# LOAD DATA

# ------------------------

filepath = "dataset/Atlantic_United_States.csv"

df = load_and_validate(filepath)

# ------------------------

# FEATURE ENGINEERING

# ------------------------

df = create_features(df)

# ------------------------

# SAVE CLEANED DATA

# ------------------------

df.to_csv(

    "output/cleaned_data.csv",

    index=False

)

# ------------------------

# PLAYLIST ANALYSIS

# ------------------------

daily_distribution, fast_risers = playlist_analysis(df)

daily_distribution.to_csv(

    "output/daily_distribution.csv",

    index=False

)

fast_risers.to_csv(

    "output/fast_risers.csv",

    index=False

)

# ------------------------

# SONG ANALYSIS

# ------------------------

longest_presence, highest_popularity = song_analysis(df)

longest_presence.to_csv(

    "output/longest_presence.csv",

    index=False

)

highest_popularity.to_csv(

    "output/highest_popularity.csv",

    index=False

)

# ------------------------

# ARTIST ANALYSIS

# ------------------------

artist_stats = artist_analysis(df)

artist_stats.to_csv(

    "output/artist_stats.csv",

    index=False

)

# ------------------------

# POPULARITY ANALYSIS

# ------------------------

popularity_stats = popularity_analysis(df)

# ------------------------

# CONTENT ANALYSIS

# ------------------------

explicit, album, duration = content_analysis(df)

explicit.to_csv(

    "output/explicit_analysis.csv",

    index=False

)

album.to_csv(

    "output/album_analysis.csv",

    index=False

)

duration.to_csv(

    "output/duration_analysis.csv",

    index=False

)

# ------------------------

# EXECUTIVE SUMMARY

# ------------------------

with open(

    "output/executive_summary.txt",

    "w",

    encoding="utf-8"

) as f:

    f.write(

        "UNITED STATES TOP 50 PLAYLIST ANALYTICS\n\n"

    )

    f.write(

        f"Total Songs : {df['song'].nunique()}\n"

    )

    f.write(

        f"Total Artists : {df['artist'].nunique()}\n"

    )

    f.write(

        f"Average Popularity : {round(df['popularity'].mean(),2)}\n"

    )

    f.write(

        f"Popularity vs Rank Correlation : "

        f"{round(popularity_stats['correlation'],2)}\n"

    )

print("\nProject Completed Successfully")