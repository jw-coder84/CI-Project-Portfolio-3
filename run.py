import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
from gspread_dataframe import get_as_dataframe

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

        title = input('Please enter title:\n')
        genre = input('Please enter a genre from the following list:\n'
                      'Adventure, Racing, FPS, RPG, Action, '
                      'Platformer, Fighting, Puzzle, Simulation, Sports, '
                      'Strategy, Visual Novel\n')
        platform = input('Please enter platform from the following list:\n'
                         'Nintendo Switch, Playstation, Xbox, '
                         'Multi-platform, Other\n')

        game_data = [title, genre, platform]
        game_data = [item.strip() for item in game_data]
        validate_data(game_data)
        print(f'The data provided is {game_data}')

        if validate_data(game_data):
            print('Data is valid!')
            break

    return game_data


def validate_data(values):
    """
    Raises error if the genre and or platform do not exist in the defined
    arrays.
    """
    genre = ['Adventure', 'Racing', 'FPS', 'RPG', 'Action', 'Platformer',
             'Fighting', 'Puzzle', 'Simulation', 'Sports', 'Strategy',
             'Visual Novel']
    platform = ['Nintendo Switch', 'Playstation', 'Xbox', 'Multi-platform',
                'Other']

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
    data.append(0)
    print("Updating games worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print("Your game has been added successfully.\n")


def game_vote():
    """
    Lets users vote for an existing game
    """
    while True:
        vote_title = input("Please enter a game title to cast your vote.\n")
        game_cell = games.find(vote_title)
        print('Submitting vote...')
        if game_cell is None:
            print(f'{vote_title} could not be found')
            continue

        vote = games.cell(game_cell.row, 4).value
        games.update_cell(game_cell.row, 4, int(vote) + 1)
        print('Thanks for voting!')
        break

    return True


def search_game():
    """
    Compiles list of top ten games based on number of votes alone.
    Alternatively, users can filter by platform and or genre.
    """
    genre = ['Adventure', 'Racing', 'FPS', 'RPG', 'Action', 'Platformer',
             'Fighting', 'Puzzle', 'Simulation', 'Sports', 'Strategy',
             'Visual Novel']
    platform = ['Nintendo Switch', 'Playstation', 'Xbox', 'Multi-platform',
                'Other']

    games_df = get_as_dataframe(games, usecols=[0, 1, 2, 3])
    count = list(range(1, 11))
    top_ten = games_df.nlargest(10, 'votes')
    top_ten['No.'] = count
    top_ten = top_ten.set_index('No.')

    print('Here you can display a top ten list of games based on the number '
          'of votes.\n'
          'You can refine the results using genre or platform as search '
          'criteria.\n')
    print('Please choose one of the following options:\n')
    print('N: No filter, G: by genre, P: by platform\n')

    search_filter = input('Please enter a search filter\n')
    search_filter = search_filter.upper()
    if search_filter == 'N':
        print(top_ten)

    elif search_filter == 'G':
        print('Adventure, Racing, FPS, RPG, Action, Platformer, '
              'Fighting, Puzzle, Simulation, Sports, Strategy, Visual Novel\n')

        while True:
            search_genre = input('Please enter genre from the above list:\n')
            if search_genre not in genre:
                print(f'{search_genre} is not valid genre.')
                continue

            filter_genre = games_df[(games_df['genre'] == search_genre)]
            print(filter_genre.nlargest(10, 'votes').reset_index(drop=True))
            break

    elif search_filter == 'P':
        print('Nintendo Switch, Playstation, Xbox, Multi-platform, Other\n')

        while True:
            search_platform = input('Please enter platform from the above list:\n')
            if search_platform not in platform:
                print(f'{search_platform} is not valid platform.')
                continue

            filter_platform = games_df[(games_df['platform'] == search_platform)]
            print(filter_platform.nlargest(10, 'votes').reset_index(drop=True))
            break
    else:
        pass

    return True


def main():
    """
    Run all program functions
    """
    user_add = input("Would you like to add a game to the list? (N/Y)\n")
    user_add = user_add.upper()
    if user_add == 'Y':
        user_game = get_game()
        update_worksheet(user_game, 'games')
    else:
        pass

    user_vote = input("Would you like to vote for a game in the list? (N/Y)\n")
    user_vote = user_vote.upper()
    if user_vote == 'Y':
        game_vote()
    else:
        pass

    user_search = input("Would you like to view the top ten games? (N/Y)\n")
    user_search = user_search.upper()
    if user_search == 'Y':
        search_game()
    else:
        pass


print('Welcome to Games Chart Data')
main()
