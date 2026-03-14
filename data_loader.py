import pandas as pd
import re


def extract_year(title):

    match = re.search(r"\((\d{4})\)", title)

    if match:
        return int(match.group(1))

    return None


def load_data():

    movies = pd.read_csv("data/movies.csv")
    ratings = pd.read_csv("data/ratings.csv")

    movies["year"] = movies["title"].apply(extract_year)

    # remove very old movies
    movies = movies[movies["year"] >= 1990]

    df = pd.merge(ratings, movies, on="movieId")

    return df


def create_movie_matrix(df):

    movie_matrix = df.pivot_table(
        index="userId",
        columns="title",
        values="rating"
    )

    movie_matrix = movie_matrix.fillna(0)

    return movie_matrix