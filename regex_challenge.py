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

my_expression = r"a"
print get_matching_words('ss')
print get_matching_words('b\wb')
print get_matching_words('b\w+b')
print get_matching_words('b\w*b')
print get_matching_words('b.?b')
print get_matching_words('a[^aeiou]*e[^aeiou]*i[^aeiou]*o[^aeiou]*u')
print get_matching_words('[aeiou]{2}$')
print get_matching_words('^[regularexpression]*$')
print get_matching_words('^[^regex]*$')
print get_matching_words(r'^.*(\w{2}).*\1$')
