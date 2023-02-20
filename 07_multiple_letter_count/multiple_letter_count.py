def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    new_list = {}

    for letter in phrase:
        new_list[letter] = new_list.get(letter, 0)+1

    return new_list
    # new_list = empty character in dictionary
    # loop through letter in phrase/word and returns 0, + 1
    # returns letter to dictionary
