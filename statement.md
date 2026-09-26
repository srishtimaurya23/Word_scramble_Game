## Project Overview
Project Title Word Scramble Challenge – Command Line Game in Python

# Description of the problem
* The aim of this project is to create a simple Word Scramble Game using Python that can be run from the command line.
* The computer picks a word at random from a pre-defined word bank and jumbles the letters. The player must identify and enter the original word. The game has different levels of difficulty so that the player can select words according to their level.
* The player has 3 tries per word. The score goes up by one every time a question is answered correctly. If the player fails to guess the word within the given tries, the correct answer is revealed.

# Project Scope
* The project is restricted to the command line interface. It consists of word selection, word scrambling, user input, answer checking, attempt handling, scoring, difficulty selection and repeat.
* The project does not use any database or third party packages.
  
# Intended Users
* Students learning basic programming in Python
* For beginners who want to practice programming through a small game.
* Users who want a simple command-line word game.

# Purposes
* The project is intended to practice:
* Variables & Data Types
* Lists and dictionaries.
* Strings and string manipulation
* if-elif-else statements using input() for and while loop
* Features
* Random Module
* Basic program logic and problem solving
* Several Python files and modular organization

# High level features
* Difficulty levels Easy, Medium and Hard
* 5 random words each game
* 3 tries for each word
* Automatic check answer
* Rating: 5 out of 5
* The total of points scored across multiple games
* Replay Feature
* Input Verification
* Module-based project structure
* Simple validation tests.

# Functional Units
* Management of words
* word_bank.py contains the word lists for the Easy, Medium and Hard levels.
* Game Logic game_logic.py selects 5 random words, scrambles them, manages attempts, checks answers and calculates the score.
* User Interaction Menus are displayed and validated user input is received in utils.py and input_handler.py.
* Score Management score_manager.py shows the score of a game and the final cumulative result.

# Requirements that are not functional
* Usability: simple and clear command line interaction.
* Performance: rapid selection of words and checking of answers.
* Reliability: invalid menu options are validated.
* Maintainability: functionality is separated in meaningful files.
* Resource Efficiency: The game utilizes small in-memory word lists.
* Portability: It uses standard-library functionality in Python.

# Program Working
* print("Welcome!")
* Pick your poison, player.
* Pick 5 random words from the chosen difficulty.
* Rearrange the characters of every expression.
* Unjumble the word.
* Player can guess the word 3 times.
* Raise the score when the answer is correct.
* Display the score after all 5 words.
* Ask the player if he wants to play again.
* Show the cumulative result when the player exits.

# Technology Used
* Programming Language: Python 3
* Module Used: random
* Interface: Command Line Interface (CLI)
