"""
URL of problem:
https://leetcode.com/problems/subdomain-visit-count/description/
"""


def main(cpdomains):
    count_dom_dict = {}
    for cpdom in cpdomains:
        [count, domain] = cpdom.split(' ')
        num_dots = domain.count('.')
        for x in range(num_dots):
            add_to_dict(count_dom_dict, domain, count)
            domain = domain.split('.', 1)[1]

        add_to_dict(count_dom_dict, domain, count)

    # pprint(count_dom_dict)
    output = [' '.join([str(count), dom])
              for dom, count in count_dom_dict.items()]
    print(output)
    # return output
    # for dot in range(num_dots):
    #     print(domains.split('.', 1))

    # for nd in range(num_dots):

    # for dom in domains:
    #     if dom not in count_dom_dict:
    #         count_dom_dict[dom] += count
    # print(count, domains)


def add_to_dict(count_dom_dict, dom, count):
    if dom not in count_dom_dict:
        count_dom_dict[dom] = int(count)
    else:
        count_dom_dict[dom] += int(count)


def test():
    d = {}
    if 'p' not in d:
        d['p'] = 6
    else:
        d['p'] += 2
    print(d)

# test()

if __name__ == '__main__':
    main([
        "900 google.mail.com",
        "50 yahoo.com",
        "1 intel.mail.com",
        "5 wiki.org"
        ])
