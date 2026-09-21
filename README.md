# Word Scramble Challenge 

A simple **command-line Word Scramble Game** made with Python.

## Features

* Easy, Medium, and Hard levels
* 5 random words per game
* 3 attempts for each word
* Score out of 5
* Option to play again

## Requirements

* Python 3.x
* VS Code or any Python-supported editor
* Git for GitHub submission

**No external packages are required.**

## Project Structure

```text
Word-Scramble-Game/
├── main.py
├── game_logic.py
├── utils.py
├── word_bank.py
├── statement.md
├── README.md
└── .gitattributes
```

`__pycache__` may be created automatically by Python and does not need to be uploaded to GitHub.

## Setup & Run

Clone the repository:

```
git clone <https://github.com/srishtimaurya23/Word_scramble_Game>
cd <Word_scramble_Game>
```

Run the game:

```
python main.py
```

On Windows, you can also use:

```
py main.py
```

## How to Play

1. Select a difficulty level.
2. Guess the scrambled word.
3. You get 3 attempts for each word.
4. Solve 5 words and check your score.
5. Choose whether to play again.

The word lists are stored in `word_bank.py`.

## GitHub Submission

After making changes:

```
git add .
git commit -m "Word Scramble Game"
git push
```

Make sure the repository includes:

* `main.py`
* `game_logic.py`
* `utils.py`
* `word_bank.py`
* `statement.md`
* `README.md`

The game should run successfully with:

```
python main.py
```

## Technologies

* Python 3
* Random Module
* Command Line Interface
* Git & GitHub
