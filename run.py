import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('games_chart')

games = SHEET.worksheet('games')

data = games.get_all_values()


def get_game():
    """
    Accept a new game from the user to be added to the spreadsheet.
    """

    while True:
        print('Please enter the following data separated by comma:')
        print('Title')
        print('Genre - options: Adventure, Racing, FPS, RPG, Action, Platformer, \
Fighting, Puzzle, Simulation, Sports, Strategy, Visual Novel')
        print('Platform - options: Nintendo Switch, Playstation, Xbox, Multi-platform, Other')
        print('Example: Doom (1993), FPS, Multi-platform')

        data_str = input('Enter Title, Genre and Platform here:\n')
        game_data = data_str.split(',')
        validate_data(game_data)
        print(f'The data provided is {data_str}')
        print(game_data)

        if validate_data(game_data):
            print('Data is valid!')
            break

    return game_data


def validate_data(values):
    """
    Raises error if the genre and or platform do not exist in the defined arrays.
    """

    genre = ['Adventure', 'Racing', 'FPS', 'RPG', 'Action', 'Platformer', 'Fighting', 'Puzzle', 'Simulation', 'Sports', 'Strategy', 'Visual Novel']
    platform = ['Nintendo Switch', 'Playstation', 'Xbox', 'Multi-platform', 'Other']

    try:
        if len(values) != 3:
            raise ValueError(
                f"Exactly 3 values required, you provided {len(values)}"
            )
        elif values[1] not in genre:
            raise ValueError(f'{values[1]} is not valid genre.')

        elif values[2] not in platform:
            raise ValueError(f'{values[2]} is not valid platform.')
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


get_game()
