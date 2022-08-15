# **_Games Chart - Project Portfolio 3_**


## [View app](https://games-chart.herokuapp.com/)

# Contents




# Objective

* The application lets the user add games to a spreadsheet. The information required for each record is the games title, genre and the platform the game is available for. 
* Another function allows users to vote for any of the games on the list. The number of votes will be recorded on the spreadsheet. 
* The final function allows users to query the spreadsheet. Users can view the top ten games on the spreadsheet based on the number of votes alone. A search by genre or platform can also be performed with the results still being organised by the number of votes. Therefore it's always a top ten chart that's being viewed, but could be the top ten adventure games or the top ten Nintendo Switch games. With a large number of games being in the list, these searches will allow users to glean further insight from the data.


# User Experience (UX)

## Design Diagram
* Initially at the beginning of the program I wanted to give the users direct access to each of the 3 functions; add game, vote for a game or search the games list. 
* My mentor suggested that this would not be ideal for the user experience as the program would need to be restarted if they wanted to run another function. 
* The alternative was to ask the user if they wanted to use each of the functions in turn, where they were given the option to choose 'Yes' or 'No'. The user would then have the opportunity to use one of more function in one run of the program.
* There was additional functionality I wanted to include for the search function. This would have allowed the user to save their search results to a file. Given the overall functionality of my program, I was advised this operation was not needed.

<br>
<details><summary><b>Design Diagram</b></summary>

![Design diagram](readme_images/design-diagram.png)
</details><br>

## Features
### Introduction
When the program begins, a welcome message is printed and the user is asked if they want to add a game to the list.

<img src="readme_images/program-intro.png" width="600" height="170"><br>

### Add Game
If the user chooses to add a game then they are asked to enter the 3 parts of data one at a time. The title, genre, then platform. The user's entered data is printed followed by messages confirming the data is valid and has been uploaded successfully.
<img src="readme_images/game-add.png" width="450" height="260"><br>
Updated spreadsheet
<br><img src="readme_images/sheet-game-add.png" width="600" height="60"><br>
If an incorrect genre or platform are entered, an error message will be displayed and the user will be prompted to enter the data again.
<br><img src="readme_images/genre-error.png" width="300" height="60"><br>
<br><img src="readme_images/platform-error.png" width="300" height="60"><br>

### Vote Game
When a user votes for a game, 1 is added to the current number of votes. If the game is not found in the spreadsheet then an error is returned and the user is asked to enter another game.
<br><img src="readme_images/game-vote.png" width="450" height="260"><br>
Updated spreadsheet.
<br><img src="readme_images/sheet-vote-game.png" width="600" height="60"><br>

### Search Spreadsheet
The user can choose to display the top ten games from the list based on votes alone, or filter by genre or platform.
Validation is also in place to ensure correct genre and platforms are entered.
<br><img src="readme_images/top-ten.png" width="450" height="260"><br>
Filtered by genre.
<br><img src="readme_images/filter-genre.png" width="450" height="260"><br>
Filtered by platform.
<br><img src="readme_images/filter-platform.png" width="450" height="260"><br>

## Future Features

