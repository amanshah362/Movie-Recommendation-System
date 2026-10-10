import streamlit as st
import requests
import pickle
import pandas as pd

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommend_movies_poster = []
    
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies_poster.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        
    return recommended_movie_names , recommend_movies_poster

st.header("Movie Recommend System")
movies_dict = pickle.load(open("model/movie_list.pkl", 'rb'))
similarity = pickle.load(open("model/similarity.pkl", 'rb'))
movies = pd.DataFrame(movies_dict)

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or Select Movie", movie_list
)

if st.button('Show Recommendation'):
    recommend_movies_name , recommend_movies_poster = recommend(selected_movie)
    
    col1, col2, col3, col4, col5 = st.columns(5)

    cols = [col1 , col2 , col3 , col4 , col5]
    
    for i in range(5):
        with cols[i]:
            st.text(recommend_movies_name[i])
            st.image(recommend_movies_poster[i])
    
    