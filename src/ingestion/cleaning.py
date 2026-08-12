import pandas as pd


def clean_movies(movies):
    # Remove the extra index column
    if "Unnamed: 0" in movies.columns:
        movies = movies.drop("Unnamed: 0", axis=1)

    # Remove spaces from column values
    movies["movie_name"] = movies["movie_name"].str.strip()
    movies["director"] = movies["director"].str.strip()

    # Remove duplicate movies
    movies = movies.drop_duplicates(subset="movie_id")

    return movies