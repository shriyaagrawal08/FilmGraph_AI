from loaders import load_movies
from cleaning import clean_movies

RAW_FILE = "data/raw/bollywood_movies.csv"
PROCESSED_FILE = "data/processed/bollywood_movies_cleaned.csv"

def run_ingestion():
    # Load the raw data
    movies = load_movies(RAW_FILE)

    # Clean the data
    cleaned_movies = clean_movies(movies)

    # Save the cleaned data to a new CSV file ( the csv file will automatically be created if it does not exist)
    cleaned_movies.to_csv(PROCESSED_FILE, index=False)  # index=False means it should not take index column while saving to csv

    print("Ingestion completed successfully!")
    print(f"Processed file saved to: {PROCESSED_FILE}")


# we are treating as the main file that runs both loaders.py and cleaning.py file.That is why we used this file as main file
if __name__ == "__main__":
    run_ingestion()

