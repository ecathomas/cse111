import random

def main():
    determiner = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, "past")
    prepositional_phrase = get_prepositional_phrase(1)
    print (f'{determiner.capitalize()} {noun} {verb} {prepositional_phrase}.')
    determiner = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, "present")
    prepositional_phrase = get_prepositional_phrase(1)
    print (f'{determiner.capitalize()} {noun} {verb} {prepositional_phrase}.')
    determiner = get_determiner(1)
    noun = get_noun(1)
    verb = get_verb(1, "future")
    prepositional_phrase = get_prepositional_phrase(1)
    print (f'{determiner.capitalize()} {noun} {verb} {prepositional_phrase}.')
    determiner = get_determiner(2)
    noun = get_noun(2)
    verb = get_verb(2, "past")
    prepositional_phrase = get_prepositional_phrase(1)
    print (f'{determiner.capitalize()} {noun} {verb} {prepositional_phrase}.')
    determiner = get_determiner(4)
    noun = get_noun(4)
    verb = get_verb(4, "present")
    prepositional_phrase = get_prepositional_phrase(1)
    print (f'{determiner.capitalize()} {noun} {verb} {prepositional_phrase}.')
    determiner = get_determiner(3)
    noun = get_noun(3)
    verb = get_verb(3, "future")
    prepositional_phrase = get_prepositional_phrase(1)
    print (f'{determiner.capitalize()} {noun} {verb} {prepositional_phrase}.')


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "two", "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        determiners = ["a", "one", "the"]
    else:
        determiners = ["two", "some", "many", "the"]

    # Randomly choose and return a determiner.
    determiner = random.choice(determiners)
    return determiner

def get_noun(quantity):
    #Return a randomly chosen noun.
    if quantity == 1: 
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    #Otherwise, this function will return one of
    #these ten plural nouns:
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    """ Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    noun = random.choice(nouns)
    return noun


def get_verb(quantity, tense):
    #Return a randomly chosen verb. 
    if tense == "past":
    #this function will return one of these ten verbs:
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    if tense == "present" and quantity == 1:
    #function will return one of these ten verbs:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    if tense == "present" and quantity != 1:
    #this function will return one of these ten verbs:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    if tense == "future":
    #this function will return one of these ten verbs:
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    """Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    verb = random.choice(verbs)
    return verb

def get_preposition():
    #Return a randomly chosen preposition
    prepositions = [
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    preposition = random.choice(prepositions)
    return preposition

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.
    
    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """
    prepositional_phrase = (f'{get_preposition()} {get_determiner(1)} {get_noun(1)}')
    return prepositional_phrase

main()