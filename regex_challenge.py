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
print get_matching_words(r'ss')
print get_matching_words(r'b\wb')
print get_matching_words(r'b\w+b')
print get_matching_words(r'b\w*b')
print get_matching_words(r'b.?b')
print get_matching_words(r'a[^aeiou]*e[^aeiou]*i[^aeiou]*o[^aeiou]*u')
print get_matching_words(r'[aeiou]{2}$')
print get_matching_words(r'^[regularexpression]*$')
print get_matching_words(r'^[^regex]*$')
print get_matching_words(r'^.*(\w{2}).*\1$')
