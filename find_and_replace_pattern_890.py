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
        shouldAdd = True
        for w, p in zip(list_chars, list_pattern):
            if w not in mapping:
                if p in mapping.values():
                    shouldAdd = False
                    break
                else:
                    mapping[w] = p
            else:
                if p != mapping[w]:
                    shouldAdd = False
                    break

        if shouldAdd:
            match_pattern.append(word)

    print(match_pattern)
    # return match_pattern


if __name__ == '__main__':
    main(words=["abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern="abb")
