def get_answer():
    """Get and clean the player's answer."""
    return input("Enter your answer: ").strip().lower()


def is_valid_replay_choice(choice):
    """Return True when the replay choice is y or n."""
    return choice in ("y", "n")


def get_replay_choice():
    """Ask the player whether another game should be played."""
    while True:
        choice = input("\nDo you want to play again? (y/n): ").strip().lower()
        if is_valid_replay_choice(choice):
            return choice
        print("Invalid choice. Please enter y or n.")
