import streamlit as st
from data_loader import load_data, create_movie_matrix
from recommender import build_similarity_matrix, recommend_movies
from poster import get_movie_poster

st.set_page_config(page_title="Movie Recommendation System")

st.title("🎬 Movie Recommendation System")
st.write("Select a movie and get recommendations based on user ratings.")

# Load dataset
df = load_data()

movie_matrix = create_movie_matrix(df)

similarity_df = build_similarity_matrix(movie_matrix)

movie_list = movie_matrix.columns.tolist()

selected_movie = st.selectbox("Select a movie", movie_list)

if st.button("Recommend Movies"):

    recommendations = recommend_movies(selected_movie, similarity_df)

    st.subheader("Recommended Movies")

    cols = st.columns(5)

    for i, movie in enumerate(recommendations.index):

        poster = get_movie_poster(movie)

        with cols[i]:

            if poster:
                st.image(poster, width=200)
            else:
                st.image(
                    "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg",
                    width=200
                )

            st.write(movie)