from game_logic import playgame
from input_handler import replaychoice
from score_manager import finalresult
def main():
    totalscore=0
    gamesplayed=0
    print("=" * 50)
    print("       WELCOME TO WORD SCRAMBLE GAME")
    print("=" * 50)
    while True:
        score=playgame()
        totalscore+=score
        gamesplayed+=1
        print("\nGames played:",gamesplayed)
        print("Total score accrued:",totalscore)
        again=replaychoice()
        if again=="n":
            break
    finalresult(gamesplayed,totalscore)
if __name__=="__main__":
    main()
