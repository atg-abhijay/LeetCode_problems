"""
URL of problem:
https://leetcode.com/problems/keyboard-row/description/
"""


def main(words):
    r1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
    r2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
    r3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
    r1_words = []
    r2_words = []
    r3_words = []
    for word in words:
        w_set = set(word.lower())
        if w_set.issubset(r1):
            r1_words.append(word)
        elif w_set.issubset(r2):
            r2_words.append(word)
        elif w_set.issubset(r3):
            r3_words.append(word)

    output = r1_words + r2_words + r3_words
    print(output)
    # return output

if __name__ == '__main__':
    main(["Hello", "Alaska", "Dad", "Peace"])
