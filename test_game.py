from utils import scramble_word
from word_bank import WORDS
from input_handler import validchoice
def testletters():
    test_word="example"
    scrambled=scramble_word(test_word)
    assert sorted(scrambled)== sorted(test_word)
def testlevels():
    assert "easy" in WORDS
    assert "medium" in WORDS
    assert "hard" in WORDS
def testwords():
    assert len(WORDS["easy"])>=5
    assert len(WORDS["medium"])>=5
    assert len(WORDS["hard"])>=5
def testvalidation():
    assert validchoice("response")
    assert validchoice("amount")
    assert not validchoice("element")
if __name__== "__main__":
    testletters()
    testlevels()
    testwords()
    testvalidation()
    print("All tests passed.")
