# Word Scramble Challenge – Project Report Draft

## 1. Introduction

Word Scramble Challenge is a Python command-line game in which the player selects a difficulty level and tries to identify scrambled words. The game uses a predefined word bank and gives the player three attempts for each word.

## 2. Problem Statement

The project provides a small interactive way to practise Python programming concepts such as variables, lists, dictionaries, strings, conditions, loops, functions, user input and the `random` module.

## 3. Objectives

- Practise basic Python programming concepts.
- Use functions and multiple Python files.
- Work with lists and dictionaries.
- Use random word selection and string operations.
- Implement input validation and simple testing.

## 4. Functional Requirements

1. The player can select Easy, Medium or Hard difficulty.
2. The program selects five random words from the selected level.
3. The program scrambles each selected word.
4. The player receives three attempts for each word.
5. The program checks answers and updates the score.
6. The program displays the game score and cumulative score.
7. The player can choose to play again.

## 5. Non-Functional Requirements

- **Usability:** The program uses simple command-line instructions.
- **Performance:** Words are stored in memory, so selection and checking are quick.
- **Reliability:** Invalid menu and replay choices are handled through validation.
- **Maintainability:** Related functions are separated into different Python files.
- **Resource efficiency:** The project uses only small in-memory lists and the Python standard library.
- **Portability:** The project can run on systems with Python 3.x.

## 6. System Architecture

The player interacts with `main.py`. The main program starts the game and connects the game logic, input handling and score modules. `game_logic.py` uses the word bank and utility functions. The design diagram is available in `docs/design.md`.

## 7. Design Diagrams

The system architecture, workflow, use case, sequence and component diagrams are provided in `docs/design.md`.

## 8. Implementation Details

The project is divided into the following files:

- `main.py` – starts the program, manages replay and cumulative score.
- `game_logic.py` – runs one game, selects words, manages attempts and checks answers.
- `word_bank.py` – stores Easy, Medium and Hard word lists.
- `utils.py` – scrambles words and handles difficulty selection.
- `input_handler.py` – handles answers and replay input validation.
- `score_manager.py` – displays game and final results.
- `test_game.py` – contains simple validation tests.

## 9. Screenshots / Results

Use the screenshots already included in `README.md` in the final PDF report.

## 10. Testing Approach

Run:

```text
python test_game.py
```

The tests check that scrambled words contain the same letters, all difficulty levels exist, each level has at least five words, and replay validation accepts only `y` or `n`.

## 11. Challenges Faced

- Dividing the program into separate Python files.
- Managing three attempts for every word.
- Making sure the scrambled word keeps the same letters.
- Handling invalid user choices.
- Keeping the score across multiple games.

## 12. Learnings and Key Takeaways

The project provided practice with functions, loops, conditions, lists, dictionaries, strings, user input, random selection, modular programming and basic testing.

## 13. Future Enhancements

- Add more words to each difficulty level.
- Add a timer for each word.
- Add a high-score system using a file.
- Add a simple graphical interface in a future version.

## 14. References

- Python 3 documentation: https://docs.python.org/3/
- Git and GitHub documentation: https://docs.github.com/
