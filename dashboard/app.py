import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="US Top 50 Playlist Analytics",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------

@st.cache_data
def load_data():

    df = pd.read_csv(
        "output/cleaned_data.csv"
    )

    df['date'] = pd.to_datetime(
        df['date']
    )

    return df


df = load_data()

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("Filters")

# Date filter

date_range = st.sidebar.date_input(

    "Date Range",

    (

        df['date'].min(),

        df['date'].max()

    )

)

# Artist filter

artist = st.sidebar.multiselect(

    "Artist",

    sorted(

        df['artist'].unique()

    )

)

# Song filter

song = st.sidebar.multiselect(

    "Song",

    sorted(

        df['song'].unique()

    )

)

# Rank filter

rank = st.sidebar.slider(

    "Rank",

    1,

    50,

    (1,50)

)

# Album filter

album = st.sidebar.multiselect(

    "Album Type",

    sorted(

        df['album_type'].unique()

    )

)

# -----------------------------
# APPLY FILTERS
# -----------------------------

if len(date_range)==2:

    start,end = date_range

    df = df[

        (df['date']>=pd.to_datetime(start))

        &

        (df['date']<=pd.to_datetime(end))

    ]

if artist:

    df = df[

        df['artist'].isin(artist)

    ]

if song:

    df = df[

        df['song'].isin(song)

    ]

if album:

    df = df[

        df['album_type'].isin(album)

    ]

df = df[

    (df['position']>=rank[0])

    &

    (df['position']<=rank[1])

]

# -----------------------------
# HEADER
# -----------------------------

st.title(

"🎵 US Top 50 Playlist Analytics Dashboard"

)

st.markdown(

"Atlantic Recording Corporation"

)

# -----------------------------
# KPI CARDS
# -----------------------------

col1,col2,col3,col4,col5=st.columns(5)

col1.metric(

    "Songs",

    df['song'].nunique()

)

col2.metric(

    "Artists",

    df['artist'].nunique()

)

col3.metric(

    "Avg Popularity",

    round(

        df['popularity'].mean(),

        1

    )

)

col4.metric(

    "Explicit %",

    round(

        df['is_explicit'].mean()*100,

        1

    )

)

col5.metric(

    "Avg Rank",

    round(

        df['position'].mean(),

        1

    )

)

st.divider()

# --------------------------------

# PLAYLIST TIMELINE

# --------------------------------

timeline = (

    df.groupby('date')

    ['popularity']

    .mean()

    .reset_index()

)

fig=px.line(

    timeline,

    x='date',

    y='popularity',

    title='Playlist Timeline'

)

st.plotly_chart(

    fig,

    use_container_width=True

)

# --------------------------------

# SONG RANKING TREND

# --------------------------------

top_song = (

    df['song']

    .value_counts()

    .head(5)

    .index

)

song_df = (

    df[

        df['song']

        .isin(top_song)

    ]

)

fig=px.line(

    song_df,

    x='date',

    y='position',

    color='song',

    title='Song Ranking Trends'

)

fig.update_yaxes(

    autorange="reversed"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

# --------------------------------

# ARTIST DOMINANCE

# --------------------------------

artist_dom = (

    df['artist']

    .value_counts()

    .head(10)

    .reset_index()

)

artist_dom.columns=[

    'artist',

    'count'

]

fig=px.bar(

    artist_dom,

    x='count',

    y='artist',

    orientation='h',

    title='Artist Dominance'

)

st.plotly_chart(

    fig,

    use_container_width=True

)

# --------------------------------

# POPULARITY VS RANK

# --------------------------------

fig=px.scatter(

    df,

    x='position',

    y='popularity',

    color='album_type',

    size='duration_min',

    title='Popularity vs Rank'

)

st.plotly_chart(

    fig,

    use_container_width=True

)

# --------------------------------

# EXPLICIT ANALYSIS

# --------------------------------

fig=px.box(

    df,

    x='is_explicit',

    y='popularity',

    title='Explicit vs Non Explicit'

)

st.plotly_chart(

    fig,

    use_container_width=True

)

# --------------------------------

# ALBUM TYPE ANALYSIS

# --------------------------------

album_df=(

    df.groupby('album_type')

    ['popularity']

    .mean()

    .reset_index()

)

fig=px.bar(

    album_df,

    x='album_type',

    y='popularity',

    title='Album Type Analysis'

)

st.plotly_chart(

    fig,

    use_container_width=True

)

# --------------------------------

# DURATION ANALYSIS

# --------------------------------

fig=px.histogram(

    df,

    x='duration_min',

    title='Song Duration Distribution'

)

st.plotly_chart(

    fig,

    use_container_width=True

)

# --------------------------------

# TOP SONGS TABLE

# --------------------------------

top_songs=(

    df.groupby('song')

    .agg(

        days_on_chart=(

            'days_on_chart',

            'max'

        ),

        avg_rank=(

            'avg_rank',

            'mean'

        ),

        popularity=(

            'popularity',

            'mean'

        )

    )

    .reset_index()

)

st.subheader(

    "Top Songs"

)

st.dataframe(

    top_songs

    .sort_values(

        'days_on_chart',

        ascending=False

    )

)