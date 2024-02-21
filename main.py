import imdb
import requests
from bs4 import BeautifulSoup
import pandas as pd

def find_movie_details(movie_title):
    # Create an IMDb access object
    ia = imdb.IMDb()

    # Search for the movie
    movies = ia.search_movie(movie_title)

    # If there are no matching movies
    if not movies:
        print("No matching movies found.")
        return None

    # Get the first matching movie (you might want to implement more logic for multiple matches)
    movie = movies[0]
    ia.update(movie)

    # Extract information from IMDbPY
    name = movie["title"]
    rating = movie.get("rating", "N/A")
    genres = ", ".join(movie.get("genres", []))
    duration = movie.get("runtimes", ["N/A"])[0]
    year = movie.get("year", "N/A")

    # Extract information from web scraping
    imdb_id = movie.getID()
    url = f"https://www.imdb.com/title/tt{imdb_id}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Save information to CSV
    csv_filename = 'movie_information.csv'
    data = {'Film Name': [name], 'Rating': [rating], 'Genre': [genres], 'Duration' : [duration], 'Year': [year]}
    df = pd.DataFrame(data, columns = ['Film Name', 'Rating', 'Genre', 'Duration', 'Year'])

    # Check if the CSV file already exists, if not, create it with headers
    try:
        existing_df = pd.read_csv(csv_filename)
        df.to_csv(csv_filename, mode='a', header=False, index=False, encoding='utf-8')
    except FileNotFoundError:
        df.to_csv(csv_filename, index=False, encoding='utf-8')

    print(f"\nMovie Information:\nFilm Name: {name}\nRating: {rating}\nGenre: {genres}\nDuration: {duration} mins\nYear: {year}")
    print(f"Details saved to {csv_filename}")

    return name, rating, genres, duration, year

if __name__ == "__main__":
    specific_movie_title = input("Enter the movie name: ")
    find_movie_details(specific_movie_title)
