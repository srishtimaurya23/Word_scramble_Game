def get_answer():
    """Get and clean the player's answer."""
    return input("Enter your answer: ").strip().lower()


def get_replay_choice():
    """Ask the player whether another game should be played."""
    while True:
        choice = input("\nDo you want to play again? (y/n): ").strip().lower()
        if choice in ("y", "n"):
            return choice
        print("Invalid choice. Please enter y or n.")
