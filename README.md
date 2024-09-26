# Card Matching Game

Welcome to the **Card Matching Game**, a command-line card-matching game built using Python. This game allows you to play with multiple players or against a computer (bot). It has various levels of difficulty and comes with both a simple and advanced game mode.

## Project Background
This project was developed as part of a university exercise to practice Python programming, game logic, and command-line interface development.

## Features
- **Multiple Difficulty Levels**: Choose from Easy, Medium, or Hard difficulty settings, each adjusting the complexity of the game.
- **Play with Friends or Against a Bot**: You can either play against another player or challenge a computer bot in the advanced mode.
- **Advanced Game Mode**: The advanced game mode adds more complexity with additional cards and gameplay strategies.
- **Simple Game Mode**: For those looking for a quick match, the simple game mode offers an easy and fast-paced experience.
- **Greek Language Support**: The game prompts and messages are displayed in Greek.

## How the Code is Structured

This project consists of several Python files, each handling different aspects of the game:

- **`start_game.py`**: The entry point for the game. When this script is run, it presents the user with the option to play the simple game or the advanced game.
- **`simple_game.py`**: Contains the main logic for the simple version of the game. It handles player inputs, card matching, score calculation, and determines the winner.
- **`advanced_game.py`**: This file handles the advanced game mode, including special cards and more complex rules.
- **`bot.py`**: Implements the logic for the computer-controlled bot in the advanced game mode. The bot will play as one of the players when selected.
- **`game_logic.py`**: Contains helper functions such as card comparisons (`equal`, `equal_ad`) and other core logic that is shared across different game modes.
- **`card_game_setup.py`**: Handles the setup of card decks, checks for No of players and calculates the points from the card mathches
## Game Modes
1. **Basic Game**:
    - Players take turns flipping cards and trying to match them.
    - The player with the most points at the end wins.
    - The game ends when all cards are matched.

2. **Advanced Game**:
    - Includes more complex rules such as playing with bots or additional cards.
    - Allows for strategies involving third cards or losing a turn based on special card combinations.

## How to Play
1. **Start the Game**:
    - When you run the game, you will be prompted to choose between the Simple and Advanced game modes.

2. **Choose the Difficulty**:
    - After selecting the game mode, you will be asked to select a difficulty level (1 for Easy, 2 for Medium, 3 for Hard).

3. **Enter Player Names**:
    - In multiplayer mode, input the names of the players.
    - If you select the bot mode, the game will automatically include the computer as a player.

4. **Flip Cards**:
    - Players take turns choosing two cards to flip.
    - If the cards match, the player gains points and continues playing.
    - If not, the next player gets their turn.

5. **Advanced Mode**:
    - In the advanced mode, special cards such as Jacks, Queens, and Kings have additional effects. For example, matching certain cards can give extra turns or skip an opponent's turn.

6. **Winning the Game**:
    - The game ends when all the cards have been matched.
    - The player with the most points wins.
    - The game will display the winner and ask if you’d like to play again or exit.
