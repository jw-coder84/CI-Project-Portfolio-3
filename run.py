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


def add_game():
    """
    Accept a new game from the user to be added to the spreadsheet.
    """
    genre = ['Adventure', 'Racing', 'FPS', 'RPG', 'Action', 'Platformer', 'Fighting', 'Puzzle', 'Simulation', 'Sports', 'Strategy', 'Visual Novel']
    print('Please enter the following data separated by comma:')
    print('Title')
    print('Genre - options: Adventure, Racing, FPS, RPG, Action, Platformer, \
Fighting, Puzzle, Simulation, Sports, Strategy, Visual Novel')
    print('Example: Doom (1993), FPS')

    data_str = input('Enter Title and Genre here:\n')


add_game()

