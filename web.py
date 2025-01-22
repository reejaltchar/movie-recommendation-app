import pickle
import streamlit as st
import pandas as pd
import requests


def fetch_poster(movie_id):
    url = 'http://api.themoviedb.org/3/movie/{}?api_key=eefc24c2413c05ac331102f73d1a7c92&language=en-US'.format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "http://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
def reco(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    reco_movies =[]
    reco_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].id


        reco_movies.append(movies.iloc[i[0]].title)
        reco_movies_poster.append(fetch_poster(movie_id))

    return reco_movies,reco_movies_poster


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title(":red[Movie Recommendation System] ")
st.subheader("Hi Cinephiles!!")
selected_movie_name = st.selectbox('What are you feeling today?',
                      movies['title'].values,index=None,placeholder="Select a movie...",)

if st.button('Suggest me!!'):
    names,poster = reco(selected_movie_name)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.caption(names[0])
        st.image(poster[0],width = 100)
    with col2:
        st.caption(names[1])
        st.image(poster[1],width = 100)
    with col3:
        st.caption(names[2])
        st.image(poster[2],width = 100)
    with col4:
        st.caption(names[3])
        st.image(poster[3],width = 100)
    with col5:
        st.caption(names[4])
        st.image(poster[4],width = 100)
