import streamlit as st
import joblib
import pandas as pd
import requests
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()

retry = Retry(
    total=5,
    connect=5,
    read=5,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"]
)

adapter = HTTPAdapter(max_retries=retry)

session.mount("https://", adapter)
session.mount("http://", adapter)

movie_list = joblib.load("Movies.pkl")
movies = pd.DataFrame(movie_list)
similarity = joblib.load("similarity.pkl")

@st.cache_data
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    params = {
        "api_key": "ecfd92a8b7ddde0bac79be160edc0b66"
    }

    response = session.get(url, params=params, timeout=20)
    data = response.json()

    return "https://image.tmdb.org/t/p/w500" + data["poster_path"]


def recommended(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse= True, key=lambda X:X[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_poster


st.title("Movie Recommended System")
options = st.selectbox(
    'How would You Like To be contacted',
    movies['title'].values
)

if st.button('Recommended'):
    names,posters = recommended(options)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

