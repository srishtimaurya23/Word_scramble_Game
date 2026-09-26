import random
from word_bank import WORDS
from utils import scramble_word,choose_difficulty
from input_handler import answer
from score_manager import gameresult
def playgame():
    difficulty=choose_difficulty()
    selected_words=random.sample(WORDS[difficulty],5)
    score=0
    print("\n" + "=" * 50)
    print("        WORD SCRAMBLE CHALLENGE")
    print("=" * 50)
    print("Difficulty:",difficulty.upper())
    print("Unscramble the letters to find the correct word.")
    print("You have 3 attempts for each word.")
    for number,word in enumerate(selected_words,1):
        scrambled=scramble_word(word)
        attempts_left=3
        print("\n" + "-" * 50)
        print("Word", number,"of 5")
        print("Scrambled word:",scrambled)
        while attempts_left > 0:
            guess=answer()
            if guess==word:
                print("Correct!")
                score+=1
                break
            attempts_left-=1
            if attempts_left>0:
                print("Wrong answer! Attempts left:",attempts_left)
            else:
                print("Wrong answer!")
                print("The correct word was:",word)
    gameresult(difficulty,score)
    return score
