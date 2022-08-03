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
Fighting, Puzzle, Simulation, Sports, Strategy, Visual Novel\n')
        print('Platform - options: Nintendo Switch, Playstation, Xbox, Multi-platform, Other\n')
        print('Example: Doom (1993),FPS,Multi-platform')

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

    check_genre = any(item in genre for item in values)
    check_platform = any(item in platform for item in values)

    try:
        if len(values) != 3:
            raise ValueError(
                f"Exactly 3 values required, you provided {len(values)}"
            )
    except ValueError as err:
        print(f"Invalid data: {err}, please try again.\n")
        return False

    try:
        if check_genre is False:
            raise ValueError(f'{values[1]} is not valid genre.')

    except ValueError as err:
        print(f"Invalid data: {err}, please try again.\n")
        return False

    try:
        if check_platform is False:
            raise ValueError(f'{values[2]} is not valid platform.')
    except ValueError as err:
        print(f"Invalid data: {err}, please try again.\n")
        return False

    return True


def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully.\n")


def game_vote():
    """
    Lets users vote for an existing game
    """

    vote_title = input("Please enter a game title to cast your vote.\n")
    game_cell = games.find(vote_title)
    games.update_cell(game_cell.row, 'votes', 'val')


def main():
    """
    Run all program functions
    """
    data = get_game()
    update_worksheet(data, 'games')


main()