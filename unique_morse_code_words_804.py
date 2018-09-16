"""
URL of problem:
https://leetcode.com/problems/unique-morse-code-words/description/
"""
import string


def main():
    # can change the list of words here
    words = ["gin", "zen", "gig", "msg"]
    letters = list(string.ascii_lowercase)
    morse_codes = [".-", "-...", "-.-.", "-..", ".",
                   "..-.", "--.", "....", "..", ".---",
                   "-.-", ".-..", "--", "-.", "---",
                   ".--.", "--.-", ".-.", "...", "-",
                   "..-", "...-", ".--", "-..-", "-.--", "--.."]
    # this creates a dictionary where the
    # key is a letter and its value is the
    # corresponding morse code for that letter
    mapping = dict(zip(letters, morse_codes))
    # a set will only store the unique
    # transformations, which is what we need
    transformations = set()
    for w in words:
        t = []
        # converting w to list beforehand
        # makes program faster as in the
        # Jewels and Stones (771) question
        word = list(w)
        for letter in word:
            # store the different
            # parts in a list
            t.append(mapping[letter])
        # using join() is much more
        # efficient than concatenating
        # repeatedly using '+'
        transf = ''.join(t)
        transformations.add(transf)

    print(transformations)
    print(len(transformations))
    # return len(transformations)

main()
