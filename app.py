import pickle
import streamlit as st


    

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])
    recomended_movies_name = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]]['movie_id']
        recomended_movies_name.append(movies.iloc[i[0]]['title'])
    return recomended_movies_name




st.header('Movie Recommendation System')


movies = pickle.load(open('artifacts/movies_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox('Enter the movie name', movie_list)



if st.button('Show Recommendation'):
    recomended_movies_name = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recomended_movies_name[0])

    with col2:
        st.text(recomended_movies_name[1])

    with col3:
        st.text(recomended_movies_name[2])

    with col4:
        st.text(recomended_movies_name[3])
        
    with col5:
        st.text(recomended_movies_name[4])


