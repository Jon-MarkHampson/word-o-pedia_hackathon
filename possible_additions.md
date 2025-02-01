# To-Do List

## Add Player prompt for player name at the start. 

## Game Display & Formatting
- ~~using ANSI escape codes to ensure the grid, hints etc always display in the same place.~~
- Improve formatting of the Leaderboard

## General Improvements
- ~~If `colour_counter == len(COLOUR_LIST)`, reset `colour_counter = 0`.~~
- Update ChatGPT call to ensure the word only appears at the front and only appears once.

## Game Features
- Allow the player to choose word directions:
  - Horizontal only.
  - Horizontal and vertical.
  - Horizontal, vertical, and diagonal.
- ~~Change wrong guesses colour to **red**.~~
- Check colours for compatibility with light mode.
- Consider using a background colour for better visibility.
- Add a timer.
- Implement a leaderboard.
- Add a game description.

## Hint System
- Apply a **20-second time penalty** for each hint.
- Keep track of which hints have been given for which words.
  - Reveal a letter for the second hint on the same word.

## Gameplay Enhancements
- Add time penalties of **10 seconds** for hints.
- Modify the game while loop to check words found against difficulty level.
- Handle vertical and diagonal words.
- Add a background for the grid.
- Implement ASCII art for visual elements.

## Topic Handling
- Allow the player to choose or randomise topics.
- Ensure the game handles large amounts of returned suggestions from Wikipedia effectively.
- Hard-code some default articles for randomisation.

## Miscellaneous
- Review colours and aesthetics for all modes.
- Ensure hints and gameplay functionality are smooth.
