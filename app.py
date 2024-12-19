import pickle
import pandas as pd
import streamlit as st
import requests
def movie_recommend(movie):
    movie_index=movies_dict[movies_dict['title'] == selected_movie].index[0]
    distances=similarity_metrics[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies =[]


    for i in movies_list:
        movie_id = movies_dict.iloc[i[0]].movie_id
        recommended_movies.append(movies_dict.iloc[i[0]].title)
    return recommended_movies

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
similarity_metrics=pickle.load(open('similarity_metrics.pkl','rb'))
movies_dict=pd.DataFrame(movies_dict)
st.title("Movie Recommender ")
selected_movie = st.selectbox(
    'Select the Movie ',
    (movies_dict['title'].values))
st.write('You selected:', selected_movie)
if st.button('Recommend'):
    recommendations=movie_recommend(selected_movie)
    st.write("Recommended Movies:")
    for i in recommendations:
          st.write(i)