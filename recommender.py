import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def build_similarity_matrix(movie_matrix):

    similarity = cosine_similarity(movie_matrix.T)

    similarity_df = pd.DataFrame(
        similarity,
        index=movie_matrix.columns,
        columns=movie_matrix.columns
    )

    return similarity_df


def recommend_movies(movie_name, similarity_df, n=5):

    scores = similarity_df[movie_name].sort_values(ascending=False)

    recommendations = scores[1:n+1]

    return recommendations