from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest

def test_get_determiner():
    # 1. Test the single determiners.
    single_determiners = ["a", "one", "the"]
    for _ in range(4):
        determiner = get_determiner(1)
        assert determiner in single_determiners

    # 2. Test the plural determiners.
    plural_determiners = ["two", "some", "many", "the"]
    for _ in range(4):
        quantity = random.randint(2, 11)
        determiner = get_determiner(quantity)
        assert determiner in plural_determiners

def test_get_noun():
    #Test single nouns.
    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    for _ in range (4):
        noun = get_noun(1)
        assert noun in single_nouns

    #Test plural nouns.
    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    for _ in range (4):
        quantity = random.randint(2, 11)
        noun = get_noun(quantity)
        assert noun in plural_nouns

def test_get_verb() :
    #Test the past tense nouns-Quantity doesn't matter
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(10):
        quantity = random.randint(1,3)
        verb = get_verb(quantity, "past")
        assert verb in past_verbs

    #Test the single present tense verbs
    single_present_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(10):
        verb = get_verb(1, "present")
        assert verb in single_present_verbs

    #Test the plural present tense verbs
    plural_present_verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    for _ in range(10):
        verb = get_verb(2, "present")
        assert verb in plural_present_verbs

    #Test the future verbs-Quantity doesn't matter
    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    for _ in range(10):
        quantity = random.randint(1,3)
        verb = get_verb(quantity, "future")
        assert verb in future_verbs

def test_get_preposition():
    prepositions = [
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(30):
        preposition = get_preposition()
        assert preposition in prepositions

def test_get_prepositional_phrase():
    single_determiners = ["a", "one", "the"]
    plural_determiners = ["two", "some", "many", "the"]
    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    prepositions = [
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(10) :
        i = random.randint(1,3)
        phrase = get_prepositional_phrase(i)
        word_in_phrase = phrase.split()
        assert len(word_in_phrase) == 3
        if i == 1:
            assert word_in_phrase[0] in prepositions
            assert word_in_phrase[1] in single_determiners
            assert word_in_phrase[2] in single_nouns
        elif 1 > 1:
            assert word_in_phrase[0] in prepositions
            assert word_in_phrase[1] in plural_determiners
            assert word_in_phrase[2] in plural_nouns

pytest.main(["-v","--tb=line","-rN",__file__])
