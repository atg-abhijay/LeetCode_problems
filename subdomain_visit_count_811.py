"""
URL of problem:
https://leetcode.com/problems/subdomain-visit-count/description/
"""


def main(cpdomains):
    """
    main method for running the program.

    Argument:
        cpdomains - list of count-paired domains
    Prints:
        list of count-paired domains that explicitly
        counts the number of visits to each subdomain
    """
    # dict where -
    #   key: domain/subdomain appearing in cpdomains
    #   value: count for that domain/subdomain
    count_dom_dict = {}
    for cpdom in cpdomains:
        # the count and domain are
        # separated by a space. obtain
        # them as separate variables.
        [count, domain] = cpdom.split(' ')
        # num_dots allows us to find all
        # subdomains for a given domain
        num_dots = domain.count('.')
        for x in range(num_dots):
            # add the (domain, count) as
            # (key, value) to the dict.
            add_to_dict(count_dom_dict, domain, count)
            # split the domain only once by
            # the '.' and set the domain as
            # the latter part of the split.
            # this new domain is now used
            # and added to the dictionary.
            domain = domain.split('.', 1)[1]

        # have to add to the dictionary outside
        # the loop for the last subdomain
        add_to_dict(count_dom_dict, domain, count)

    # we get the domain/subdomains from the dict along
    # with the counts for each of them. we then join
    # them (separate them by a ' ') and form a string.
    # the string gets added to the output list.
    output = [' '.join([str(count), dom])
              for dom, count in count_dom_dict.items()]

    print(output)
    # return output


def add_to_dict(count_dom_dict, dom, count):
    """
    function which adds a (key, value) pair to
    a dictionary.

    if the key 'dom' doesn't exist in the dict,
    initialize it in the dict with the value 'count'.
    if it exists in the dict, increase the value
    associated with it by 'count'.
    Arguments:
        count_dom_dict - dict where
                            key: domain/subdomain
                            value: count
        dom - a domain/subdomain
        count - (string value) count for
                that domain/subdomain
    """
    if dom not in count_dom_dict:
        count_dom_dict[dom] = int(count)
    else:
        count_dom_dict[dom] += int(count)


if __name__ == '__main__':
    main([
        "900 google.mail.com",
        "50 yahoo.com",
        "1 intel.mail.com",
        "5 wiki.org"
        ])
