import re

def get_matching_words(regex):
    results = []
    words = [
        "baby",
        "baseball",
        "denver",
        "facetious",
        "issue",
        "mattress",
        "obsessive",
        "paranoia",
        "rabble",
        "union",
        "volleyball",
    ]
    for word in words:
        if re.search(regex, word):
            results.append(word)

    return results


def get_regex_patterns():
    count = 1
    patterns = [
        r'^\w*(s)\1\w*$',
        r'^\w*b.b\w*$',
        r'^\w*b.+b\w*$',
        r'^\w*b.*b\w*$',
        r'^\w*b.?b\w*$',
        r'^\w*a[^aiou]*e[^aeou]*i[^aeiu]*o[^aeio]*u\w*$',
        r'^\w*[aeiou]{2}$',
        r'^[regular expression]+$',
        r'^[^regex]+$',
        r'^\w*([a-z])\1\w*\1\w*$'
    ]
    print ' '
    print '---------'
    for pattern in patterns:
        print count, pattern
        print get_matching_words(pattern)
        print '---------'
        count += 1
    print ' '


# my_expression = r"a"
# print get_matching_words(my_expression)

get_regex_patterns()
