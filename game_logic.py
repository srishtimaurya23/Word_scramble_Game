from word_bank import WORDS
from utils import scramble_word, choose_difficulty
from input_handler import answer
from score_manager import gameresult
import random
def playgame():
    # grab difficulty and select words
    lvl = choose_difficulty()
    pool = random.sample(WORDS[lvl], 5)
    print("-" * 20)
    print("WORD SCRAMBLE CHALLENGE")
    print("-" * 20)
    print("Difficulty:", lvl.upper())
    print("Unscramble the letters to find the correct word.")
    print("You have 3 attempts for each word.")
    score = 0
    for i, w in enumerate(pool, 1):
        mixed = scramble_word(w)
        tries = 3
        print("\n" + "-" * 50)
        print("Word", i, "of 5")
        print("Scrambled word:", mixed)
        while tries > 0:
            guess = answer()
            if guess == w:
                print("Correct!")
                score = score + 1
                break
            tries -= 1
            if tries > 0:
                print("Wrong answer! Attempts left:", tries)
            else:
                print("Wrong answer!")
                print("The correct word was:", w)
    gameresult(lvl, score)
    return score