def show_game_result(difficulty, score):
    """Display the result of one game."""
    print("\n" + "=" * 50)
    print("                 RESULTS")
    print("=" * 50)
    print("Difficulty:", difficulty.upper())
    print("Score:", score, "/ 5")

    if score == 5:
        print("Perfect Score!")
    elif score >= 3:
        print("Great job!")
    elif score >= 1:
        print("Good try!")
    else:
        print("Keep practicing!")


def show_final_result(games_played, total_score):
    """Display the cumulative result when the player exits."""
    print("\n" + "=" * 50)
    print("             GAME OVER")
    print("=" * 50)
    print("Total Games Played:", games_played)
    print("Final Cumulative Score:", total_score)
    print("Thanks for playing!")
