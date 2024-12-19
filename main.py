import pickle
import pandas as pd
import streamlit as st
import requests
def movie_recommend(movie):
    movie_index=movies_dict[movies_dict['title'] == selected_movie].index[0]
    distances=similarity_metrics[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies =[]
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies_dict.iloc[i[0]].movie_id
        recommended_movies.append(movies_dict.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a64b55747ebb8aaac2fd53447bbda1df&language=en-US'.format(movie_id))
    data=response.json()
    return 'https://images.tmdb.org/t/p/w500/'+ data['poster_path']

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
similarity_metrics=pickle.load(open('similarity_metrics.pkl','rb'))
movies_dict=pd.DataFrame(movies_dict)
st.title("Movie Recommender ")
selected_movie = st.selectbox(
    'Select the Movie ',
    (movies_dict['title'].values))
st.write('You selected:', selected_movie)
if st.button('Recommend'):
    names,posters=movie_recommend(selected_movie)
    col1,col2,col3,col4,col5 = st.columns(5)
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