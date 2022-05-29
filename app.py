import pandas as pd
import streamlit as st
import pickle
import requests





def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3049ee0bf6dcaf3ac7a13904760bd5f3&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]


    recommended_movies = []
    recommended_movie_posters = []
    recommend_genres = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movie_posters


movies_dict = pickle.load(open('movie_dictionary.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similar.pkl', 'rb'))


st.title('My Movie Buddy')

selected_movie_name = st.selectbox(
    'Choose a movie',
    movies['title'].values
)

if st.button('Show Recommendations'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.image(posters[0])
        st.markdown(names[0])

    with col2:
        st.image(posters[1])
        st.markdown(names[1])

    with col3:
        st.image(posters[2])
        st.markdown(names[2])

    with col4:
        st.image(posters[3])
        st.markdown(names[3])

    with col5:
        st.image(posters[4])
        st.markdown(names[4])

    with col6:
        st.image(posters[5])
        st.markdown(names[5])

















