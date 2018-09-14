"""
URL of problem:
https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
"""


def main(st):
    st_list = st.split(' ')
    output = []
    for word in st_list:
        w_list = list(word)
        w_list.reverse()
        output.append(''.join(w_list))

    # output = [''.join(list(word).reverse()) for word in st_list]
    print(' '.join(output))


if __name__ == '__main__':
    main(input("Input a string: "))
