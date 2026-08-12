# this file just loads the raw/ folder csv file here
import pandas as pd


def load_movies(file_path):
    movies = pd.read_csv(file_path)
    return movies


# we need to call the above method like this -> movies = load_movies("data/raw/bollywood_movies.csv")