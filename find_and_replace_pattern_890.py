"""
URL of problem:
https://leetcode.com/problems/find-and-replace-pattern/description/
"""


def main(words, pattern):
    match_pattern = []
    for word in words:
        mapping = {}
        list_chars = [char for char in word]
        list_pattern = [char for char in pattern]
        # assume that the word
        # matches the given pattern
        shouldAdd = True
        # iterating character by character
        # over the word and the pattern
        for w, p in zip(list_chars, list_pattern):
            # if the word_letter has
            # not been added to the map
            if w not in mapping:
                # if the word_letter maps to a
                # pattern_letter which is already
                # assigned to another word_letter,
                # the word does not match the pattern
                if p in mapping.values():
                    shouldAdd = False
                    break
                else:
                    mapping[w] = p

            # word_letter exists in the map.
            # if pattern_letter doesn't match
            # the pattern_letter assigned to
            # this word_letter, the word does
            # not match the pattern
            else:
                if p != mapping[w]:
                    shouldAdd = False
                    break

        # if shouldAdd was not negated
        # anywhere in the loop above,
        # the word matches the pattern
        if shouldAdd:
            match_pattern.append(word)

    print(match_pattern)
    # return match_pattern


if __name__ == '__main__':
    main(words=["abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern="abb")
