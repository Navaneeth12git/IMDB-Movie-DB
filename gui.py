import PySimpleGUI as sg
from main import find_movie_details

def create_gui():
    layout = [
        [sg.Text('Enter Movie Name')],
        [sg.Input(key='movie_title'), sg.OK(), sg.Cancel()],
        [sg.Text('', size=(30, 1), key='status_message', text_color='black')],
    ]

    window = sg.Window('Enter Movie Name', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Cancel':
            window.close()
            return None

        if event == 'OK':
            movie_title = values['movie_title'].strip()

            if movie_title:
                window['status_message'].update('Searching...', text_color='black')
                window.refresh()

                result = find_movie_details(movie_title)

                if result:
                    name, rating, genres, duration, year = result
                    display_results(name, rating, genres, duration, year)
                    window['status_message'].update('Movie found!', text_color='green')
                else:
                    window['status_message'].update('Movie not found. Please enter a valid title.', text_color='red')

    window.close()

def display_results(name, rating, genres, duration, year):
    layout = [
        [sg.Text(f'Movie: {name}', size=(50, 1), text_color='blue', font=('Helvetica', 14, 'bold'))],
        [sg.Text(f'Rating: {rating}', size=(50, 1), text_color='green', font=('Helvetica', 12))],
        [sg.Text(f'Genres: {genres}', size=(50, 1), text_color='orange', font=('Helvetica', 12))],
        [sg.Text(f'Duration: {duration} mins', size=(50, 1), text_color='purple', font=('Helvetica', 12))],
        [sg.Text(f'Year: {year}', size=(50, 1), text_color='red', font=('Helvetica', 12))],
        [sg.OK(button_color=('white', 'blue'))]
    ]

    window = sg.Window('Movie Rating and Genres', layout, font='Italian 12')
    event, values = window.read(close=True)

def main():
    create_gui()

if __name__ == "__main__":
    main()
