"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    letters = {}
    single_letters = 0

    # add letters to dict
    for letter in word:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    # check number of each letter
    for letter in letters:
        if (letters[letter] % 2) is not 0:
            single_letters += 1

    # allow for one single letter
    if single_letters < 2:
        return True
    else:
        return False 


if __name__ == '__main__':

    # print is_anagram_of_palindrome('abba')
    # print is_anagram_of_palindrome('abd')

    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
