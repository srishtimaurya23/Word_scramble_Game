import random
def scramble_word(word):
    word_list=list(word)
    random.shuffle(word_list)
    return ''.join(word_list)
def choose_difficulty():
    print("\nChoose Difficulty")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    while True:
        choice=input("Enter your choice (1-3): ").strip()
        if choice=="1":
            return "easy"
        elif choice=="2":
            return "medium"
        elif choice=="3":
            return "hard"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")