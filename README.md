# IMDB Movie DB

## Overview
IMDB Movie DB is a Python application that allows users to search for movie information on IMDb. It uses IMDbPY for fetching basic movie details and performs web scraping to get additional information.

## Features
- Search for a movie by entering its name.
- Displays movie details such as title, rating, genres, duration, and release year.
- Saves movie details to a CSV file for future reference.

## Getting Started
1. Clone the repository: `git clone https://github.com/Navaneeth12git/IMDB-Movie-DB.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python gui.py`

## Dependencies
- IMDbPY
- requests
- BeautifulSoup
- pandas
- PySimpleGUI

## Usage
1. Enter the name of the movie in the input field.
2. Click the 'OK' button to search for the movie.
3. View the movie details in the GUI window.
4. Movie details are saved to `movie_information.csv`.
