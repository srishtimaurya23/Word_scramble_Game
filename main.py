from game_logic import play_game
from input_handler import get_replay_choice
from score_manager import show_final_result
def main():
    total_score = 0
    games_played = 0
    print("=" * 50)
    print("       WELCOME TO WORD SCRAMBLE GAME")
    print("=" * 50)
    while True:
        score = play_game()
        total_score += score
        games_played += 1
        print("\nGames played:", games_played)
        print("Total score accrued:", total_score)
        again = get_replay_choice()
        if again == "n":
            break
    show_final_result(games_played, total_score)
if __name__ == "__main__":
    main()
