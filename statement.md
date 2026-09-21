# Problem Statement

## Word Scramble Challenge

### 1. Project Title

**Word Scramble Challenge – A Python Command-Line Game**

### 2. Problem Statement

The objective of this project is to develop a simple command-line based **Word Scramble Game using Python**.

In this game, the computer selects a word randomly from a predefined word bank and rearranges its letters. The player has to identify and enter the original word. The game provides different difficulty levels so that the player can choose words according to their level.

The player gets **3 attempts for each word**. A correct answer increases the player's score by one. If the player is unable to guess the word within the given attempts, the correct answer is displayed.

### 3. Objectives

The project is designed to practice the following Python programming concepts:

* Variables and data types
* Lists and dictionaries
* Strings and string operations
* User input using `input()`
* `if-elif-else` conditional statements
* `for` and `while` loops
* Functions
* The `random` module
* Basic program logic and problem solving
* Using multiple Python files to organize a program

### 4. Working of the Program

The program follows these steps:

1. Display the welcome message.
2. Ask the player to select a difficulty level.
3. Select 5 random words from the selected difficulty.
4. Scramble the letters of each word.
5. Display the scrambled word.
6. Allow the player 3 attempts to guess the word.
7. Increase the score when the answer is correct.
8. Display the final score after all 5 words.
9. Ask the player whether they want to play again.

### 5. Difficulty Levels

The game contains three categories:

* **Easy:** Short and simple words.
* **Medium:** Moderately difficult words.
* **Hard:** Longer and more challenging words.

Each category contains a list of words stored in `word_bank.py`.

### 6. File Organization

The project is divided into separate files:

* **`main.py`** – Controls the execution of the program.
* **`game_logic.py`** – Contains the main game functions and logic.
* **`utils.py`** – Contains helper functions.
* **`word_bank.py`** – Contains the word lists for different difficulty levels.

### 7. Expected Output

The program should provide an interactive game where the user can select a difficulty level, solve scrambled words, receive feedback, and see their final score.

The project demonstrates the practical use of basic Python programming concepts to create a small, functional command-line application.

### 8. Technology Used

**Programming Language:** Python 3

**Module Used:** `random`

**Interface:** Command Line Interface (CLI)

**Version Control:** Git and GitHub
