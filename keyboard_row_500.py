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
    output = []
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

        # if w_set.issubset(r) evaluates to True
        # for any r in [r1, r2, r3], the whole
        # expression is True and we append the word
        # to the output list.

        # here we only have 3 sets. but it's useful
        # to use the any() function if we have more
        # than 3 sets. it allows us to avoid having
        # to write multiple if-elif statements (like
        # we did in the previous version of the solution)
        if any(w_set.issubset(r) for r in [r1, r2, r3]):
            output.append(word)

    print(output)
    # return output

if __name__ == '__main__':
    main(["Hello", "Alaska", "Dad", "Peace"])
