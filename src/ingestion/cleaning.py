import pandas as pd


def clean_movies(movies):
    # Remove the extra index column
    if "Unnamed: 0" in movies.columns:
        movies = movies.drop("Unnamed: 0", axis=1)

    # Remove spaces from column values, i.e., "  3 idiots  " should become "3 idiots"
    text_columns = [
        "movie_id",
        "movie_name",
        "genre",
        "overview",
        "director",
        "cast"
    ]

    for column in text_columns:
        movies[column] = movies[column].str.strip()

    # Remove duplicate movies
    movies = movies.drop_duplicates(subset="movie_id")

    return movies