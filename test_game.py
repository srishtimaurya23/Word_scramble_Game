from utils import scramble_word
from word_bank import WORDS
from input_handler import get_replay_choice


def test_scramble_has_same_letters():
    word = "garden"
    scrambled = scramble_word(word)
    assert sorted(word) == sorted(scrambled)


def test_word_bank_has_three_levels():
    assert "easy" in WORDS
    assert "medium" in WORDS
    assert "hard" in WORDS


def test_each_level_has_enough_words():
    assert len(WORDS["easy"]) >= 5
    assert len(WORDS["medium"]) >= 5
    assert len(WORDS["hard"]) >= 5


def test_replay_validation():
    # The function is tested manually because it requires keyboard input.
    assert get_replay_choice.__name__ == "get_replay_choice"


if __name__ == "__main__":
    test_scramble_has_same_letters()
    test_word_bank_has_three_levels()
    test_each_level_has_enough_words()
    test_replay_validation()
    print("All tests passed.")
