"""
URL of problem:
https://leetcode.com/problems/keyboard-row/description/
"""


def main(words):
    """
    main method for running the program.
    Argument:
        words - a list of words containing
                only alphabets

    Prints:
        a list of words each of which only
        contain letters from one row of
        alphabets on the keyboard
    """
    # making the three rows (as sets)
    # of alphabets on the keyboard
    r1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
    r2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
    r3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
    # lists to store words that
    # consist of letters from only
    # r1 or r2 or r3
    r1_words = []
    r2_words = []
    r3_words = []
    for word in words:
        # we convert the word to a set
        # since we are only concerned with
        # the unique letters in the word.
        # we do not care about their quantities.
        w_set = set(word.lower())
        # we check if the word set is a
        # subset of any of the 3 sets (rows)
        # of alphabets on the keyboard. if it
        # is a subset, that means that that word
        # was made only using letters from that
        # specific row and fits our requirements.
        # we add that word to the list.
        if w_set.issubset(r1):
            r1_words.append(word)
        elif w_set.issubset(r2):
            r2_words.append(word)
        elif w_set.issubset(r3):
            r3_words.append(word)

    # for this specific question, we actually
    # don't need to have 3 separate lists for
    # the words since we ended up adding them
    # here, but they're useful if we're interested
    # in words made from a specific row.
    output = r1_words + r2_words + r3_words
    print(output)
    # return output

if __name__ == '__main__':
    main(["Hello", "Alaska", "Dad", "Peace"])
