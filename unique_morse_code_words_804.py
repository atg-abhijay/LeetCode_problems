"""
URL of problem: https://leetcode.com/problems/unique-morse-code-words/description/
"""
import string
from pprint import pprint

def main():
    letters = list(string.ascii_lowercase)
    morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    mapping = dict(zip(letters, morse_codes))
    # pprint(mapping)
    transformations = set()
    words = ["gin", "zen", "gig", "msg"]
    for w in words:
        t = []
        word = list(w)
        for letter in word:
            # print(letter)
            t.append(mapping[letter])
        transf = ''.join(t)
        # print(transf)
        transformations.add(transf)

    print(len(transformations))
    # return len(transformations)

# main(input("Give list of words: "))
main()
