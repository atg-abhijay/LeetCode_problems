"""
URL of problem:
https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
"""


def main(st):
    """
    main method for running the program.
    Argument:
        st - any string
    Prints:
        Reverse the order of characters in each word
        within a sentence while still preserving
        whitespace and initial word order.
    """
    # separate the words
    st_list = st.split(' ')
    output = []
    for word in st_list:
        # convert the word to a list of chars,
        # reverse the list, combine the list
        # to get the reversed word and add
        # that word to the 'output' list
        w_list = list(word)
        w_list.reverse()
        output.append(''.join(w_list))

    # join the words in the output list
    print(' '.join(output))
    # return ' '.join(output)


if __name__ == '__main__':
    main(input("Input a string: "))
