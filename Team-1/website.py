# import streamlit as st
# import pickle
# import pandas as pd
# import requests
# def fetch_poster(movie_id):
# #    response= requests.get()
# #    data=response.json()
# #    return data['poster_path']
# def recommended(movie):
#     movie_index=movies[movies['title']==movie].index[0]
#     distances=similarity[movie_index]
#     movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
#     recommended_movies=[]
#     recommended_movies_posters=[]
#     for i in movie_list:
#         movie_id=i[0]
#         recommended_movies.append(movies.iloc[i[0]].title)
#         # recommended_movies_posters.append(fetch_poster(movie_id))
#     return recommended_movies
#
# movie_dict=pickle.load(open('movies_dict.pkl','rb'))
# movies=pd.DataFrame(movie_dict)
#
# similarity=pickle.load(open('similarity.pkl','rb'))
# st.title('Movie Reccomendation System')
#
# selected_movie_name = st.selectbox(
# 'How would you like to be contacted?',
# movies['title'].values)
# if st.button('Recommend'):
#     recommendations=recommended(selected_movie_name)
#     for i in recommendations:
#         st.write(i)






import pickle
import streamlit as st
import requests
import pandas as pd

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=037b4ab3d95b71d0de81b536f8245bb0&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters
movie_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

st.header('Movie Recommender System')


movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    col6, col7, col8, col9, col10= st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    st.text("                                ")
    st.text("                                ")
    st.text("                                ")
    with col6:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
    with col7:
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])
    with col8:
        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])
    with col9:
        st.text(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])
    with col10:
        st.text(recommended_movie_names[9])
        st.image(recommended_movie_posters[9])




